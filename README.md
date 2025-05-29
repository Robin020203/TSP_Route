# Routeberekening voor leveringen
Dit project berekent automatisch de optimale leverroute op basis van een lijst adressen.

De berekening gebruikt:
- Adressen (csv bestand gedownload via Google Maps)
- Coördinaten csv (opgebouwd)
- Afstandsmatrix csv (opgebouwd met NearestNeaighbour of TSP algoritme)

Verder wordt de route gevisualiseerd en de totale afstand wordt berekend.

## TSP of NearestNeigbour:

- Gebruik TSP (Traveling Salesman Problem) voor de kortste route door alle locaties tot de beginlocatie.
- Gebruik NearestNeighbour voor telkens naar de kortste volgende locatie te gaan en zo terug naar de beginlocatie.

---

## Projectstructuur

| Bestand                                 | Functie                                                   |
|-----------------------------------------|---------------------------------------------------------- |
| `1_Adress->Coordinate.py`               | Zet adressen om naar GPS-coördinaten (latitude/longitude) |
| `2_DistanceMatrix.py`                   | Maakt een afstandsmatrix met OpenRouteService             |
| `3_RouteBerekening_NearestNeighbour.py` | Berekent de optimale NearestNeighbour route               |
| `3_RouteBerekening.py`                  | Berekent de optimale TSP route                            |
| `4_VisualRoute_NearestNeighbour.py`     | Visualiseert de NearestNeighbour route op een kaart       |
| `4_VisualRoute_TSP.py`                  | Visualiseert de TSP route op een kaart                    |
| `5_KilometerBerekening.py`              | Berekent de afstand tussen alle punten in km              |

---

## Installatie

1. Clone de repository:
   ```bash
   git clone https://github.com/Robin020203/TSP_Route.git
   cd Routeberekening

2. Installeer vereiste Python-pakketten:

`pip install pandas numpy matplotlib openrouteservice ortools`

3. Vraag je OpenRouteService API-sleutel aan en voeg hem toe in 2_DistanceMatrix.py.

`https://openrouteservice.org/dev/#/api-docs`
   
5. Run in deze volgorde (verander overal de namen van de CSV files die worden gemaakt, aangegeven in comments):
   
`1_Adress->Coordinate.py` (+ Laad het bestand in)

`2_DistanceMatrix.py` (+ Voeg API-sleutel toe)

`3_RouteBerekening_NearestNeighbour.py` of `3_RouteBerekening_TSP.py`

`4_VisualRoute_NearestNeighbour.py` of `4_VisualRoute_TSP.py`

`5_KilometerBerekening.py` (standaard met TSP)

