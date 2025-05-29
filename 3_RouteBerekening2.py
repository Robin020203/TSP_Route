import pandas as pd
import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Laad afstandsmatrix
afstand_matrix = pd.read_csv("2_DistanceMatrix_openrouteservice.csv").to_numpy()

def create_data_model():
    data = {}
    data['distance_matrix'] = afstand_matrix.astype(int).tolist()
    data['num_vehicles'] = 1
    data['depot'] = 63  # Startpunt (vervang dit eventueel door je gewenste index)
    return data

def solve_tsp(data):
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        return data['distance_matrix'][manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    solution = routing.SolveWithParameters(search_parameters)

    if not solution:
        return None

    index = routing.Start(0)
    route = []
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        index = solution.Value(routing.NextVar(index))
    route.append(manager.IndexToNode(index))
    return route

# Uitvoeren
data = create_data_model()
optimale_route = solve_tsp(data)

if optimale_route:
    df_resultaat = pd.DataFrame({'index': optimale_route})
    df_resultaat.to_csv("3_RouteOptimaal_ORtools.csv", index=False)
    print("✅ Route opgeslagen als 3_RouteOptimaal_ORtools.csv")
else:
    print("❌ Geen oplossing gevonden.")
