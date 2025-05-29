import pandas as pd
import folium

# Laad originele adressen met coördinaten en volledige info
adressen_df = pd.read_csv("1_Zone7_met_coordinaten.csv")

# Laad de ORTools-resultaatvolgorde (indexen uit afstandsmatrix)
route_df = pd.read_csv("3_RouteOptimaal_ORtools.csv")
route_indexen = route_df["index"].astype(int).tolist()

# Bouw DataFrame in volgorde van de berekende route
geordend_df = adressen_df.iloc[route_indexen].reset_index(drop=True)

# Startpositie: eerste punt
start_location = [geordend_df.iloc[0]['latitude'], geordend_df.iloc[0]['longitude']]

# Maak een kaart
m = folium.Map(location=start_location, zoom_start=15)

# Voeg markers toe voor alle punten
for i, row in geordend_df.iterrows():
    folium.Marker(
        [row['latitude'], row['longitude']],
        popup=f"{i}: {row['volledig_adres']}",
        tooltip=row['straat + huisnummer'],
        icon=folium.Icon(color="green" if i == 0 else "blue")
    ).add_to(m)

# Voeg route-lijn toe
route_coords = geordend_df[['latitude', 'longitude']].values.tolist()
folium.PolyLine(route_coords, color="red", weight=3, opacity=0.8).add_to(m)

# Sla kaart op
m.save("4_VisueleRoutekaart.html")
print("Routekaart opgeslagen als '4_VisueleRoutekaart.html'")
