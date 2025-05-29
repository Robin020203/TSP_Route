import pandas as pd
import openrouteservice
import numpy as np
import time

# openrouteservice API-sleutel (VUL ZELF AAN)
API_KEY = "5b3ce3597851110001cf6248bd3198958c8a406bb2e2fe4994b20d50"
# VOORBEELD: API_KEY = "5b3...20d50"
client = openrouteservice.Client(key=API_KEY)

# Lees coördinaten
df = pd.read_csv("1_Zone7_met_coordinaten.csv")
locaties = df[['longitude', 'latitude']].values.tolist()

n = len(locaties)
matrix = np.zeros((n, n))

# Vraag afstanden op in batches
batch_size = 50 # anders was matrix te groot (opgesplitst)

for i in range(0, n, batch_size):
    origins = locaties[i:i + batch_size]
    for j in range(0, n, batch_size):
        destinations = locaties[j:j + batch_size]

        try:
            result = client.distance_matrix(
                locations=origins + destinations,
                #profile='driving-car', # AUTO AFSTAND
                #profile='cycling-regular', # FIETS AFSTAND
                profile='foot-walking', # TE VOET
                metrics=['distance'],
                sources=list(range(len(origins))),
                destinations=list(range(len(origins), len(origins) + len(destinations))),
                units='m'
            )

            for idx_o, row in enumerate(result['distances']):
                for idx_d, val in enumerate(row):
                    matrix[i + idx_o][j + idx_d] = val
            time.sleep(1)

        except Exception as e:
            print(f"Fout bij blok ({i}, {j}): {e}")

# Opslaan als CSV (verander naam en update in 3_RouteBerekening en 5_Kilometerberekening)
pd.DataFrame(matrix).to_csv("2_DistanceMatrix_openrouteservice.csv", index=False)
print("Volledige afstandsmatrix opgeslagen als '2_DistanceMatrix_openrouteservice.csv'")
