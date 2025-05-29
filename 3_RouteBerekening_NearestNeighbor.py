import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Laad afstandsmatrix en coördinaten
afstand_matrix = pd.read_csv("2_DistanceMatrix_openrouteservice.csv").to_numpy()
adres_df = pd.read_csv("1_Zone7_met_coordinaten.csv")

# Startpunt (gekozen): Voorbeeld: Steenweg 10 (gevonden op index 63)
start_index = 63 # VERANDER DEZE NAAR INDEX VAN GEKOZEN STARTPUNT

def nearest_neighbor_fixed_start(matrix, start):
    n = len(matrix)
    visited = [start]
    current = start
    while len(visited) < n:
        next_city = np.argmin([
            matrix[current][j] if j not in visited else np.inf
            for j in range(n)
        ])
        visited.append(next_city)
        current = next_city
    return visited + [start]  # terug naar start

# Bereken de route
route = nearest_neighbor_fixed_start(afstand_matrix, start_index)
route_df = adres_df.iloc[route].reset_index(drop=True)
route_df["matrix_index"] = route  # voeg matrix-index toe aan optimale route (nodig voor afstand te berekenen)

# Oplsaan als CSV (verander naam en update in 4_VisualRoute en 5_Kilometerberekening)
route_df.to_csv("3_RouteOptimaal.csv", index=False)
print("Optimale route opgeslagen als '3_RouteOptimaal.csv'")

# Visualiseer
plt.figure(figsize=(10, 8))
plt.plot(route_df['longitude'], route_df['latitude'], 'o-', markersize=5)
for i, row in route_df.iterrows():
    plt.text(row['longitude'], row['latitude'], str(i), fontsize=8)
plt.title("Optimale bezorgronde vanaf Jetsesteenweg 610")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.tight_layout()
plt.show()
