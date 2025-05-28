# Routeberekening voor leveringen
Dit project berekent automatisch de optimale leverroute op basis van een lijst adressen.

De berekening gebruikt:
- Adressen (csv bestand gedownload via Google Maps)
- Coördinaten csv (opgebouwd)
- Afstandsmatrix csv via OpenRouteService en een eenvoudige nearest neighbor-algoritme.

Verder wordt de route gevisualiseerd en de totale afstand wordt berekend.

---

## Projectstructuur

| Bestand                          | Functie                                                   |
|----------------------------------|---------------------------------------------------------- |
| `1_Adress->Coordinate.py`        | Zet adressen om naar GPS-coördinaten (latitude/longitude) |
| `2_DistanceMatrix.py`            | Maakt een afstandsmatrix met OpenRouteService             |
| `3_RouteBerekening.py`           | Berekent de optimale route (start: Jetsesteenweg 610)     |
| `4_VisualRoute.py`               | Visualiseert de route op een kaart                        |
| `5_KilometerBerekening.py`       | Berekent de afstand tussen alle punten in km              |
| `3_RouteOptimaal.csv`            | Resultaat: geoptimaliseerde route met coördinaten         |

---

## Installatie

1. Clone de repository:
   ```bash
   git clone https://github.com/Robin020203/Routeberekening.git
   cd Routeberekening

2. Installeer vereiste Python-pakketten:

`pip install pandas numpy matplotlib openrouteservice`

3. Vraag je OpenRouteService API-sleutel aan en voeg hem toe in 2_DistanceMatrix.py.

`https://openrouteservice.org/dev/#/api-docs`
   
5. Run in deze volgorde (verander overal de namen van de CSV files die worden gemaakt, plaats staat duidelijk aangegeven in comments):
   
`1_Adress->Coordinate.py` (Laad het bestand in)

`2_DistanceMatrix.py` (Voeg API-sleutel toe en kies ook je profile: te voet, met de fiets of met de auto)

`3_RouteBerekening.py`

`4_VisualRoute.py`

`5_KilometerBerekening.py`

