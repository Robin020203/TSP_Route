import pandas as pd

# Laad afstandsmatrix
afstand_matrix = pd.read_csv("2_DistanceMatrix_openrouteservice.csv").to_numpy()

# Laad geoptimaliseerde route inclusief matrix_index

#df = pd.read_csv("3_RouteOptimaal.csv")
#route = df["matrix_index"].astype(int).tolist()
df = pd.read_csv("3_RouteOptimaal_ORtools.csv")
route = df["index"].astype(int).tolist()


# Bereken afstanden
tussenafstand_km = []
totale_afstand_km = 0

for i in range(len(route) - 1):
    van = route[i]
    naar = route[i + 1]
    afstand_m = afstand_matrix[van][naar]
    afstand_km = afstand_m / 1000
    tussenafstand_km.append((van, naar, round(afstand_km, 3)))
    totale_afstand_km += afstand_km

# Toon resultaten
for van, naar, afstand in tussenafstand_km:
    print(f"{van} → {naar}: {afstand} km")

print(f"\nTotale afstand van de route: {totale_afstand_km:.2f} km")
