import pandas as pd
import folium

# Laad de CSV met de berekende route
df = pd.read_csv("3_RouteOptimaal.csv")

# Startpositie: eerste punt
start_location = [df.iloc[0]['latitude'], df.iloc[0]['longitude']]

# Maak een kaart
m = folium.Map(location=start_location, zoom_start=15)

# Voeg markers toe voor alle punten
for i, row in df.iterrows():
    folium.Marker(
        [row['latitude'], row['longitude']],
        popup=f"{i}: {row['volledig_adres']}",
        tooltip=row['straat + huisnummer'],
        icon=folium.Icon(color="green" if i == 0 else "blue")
    ).add_to(m)

# Voeg route-lijn toe
route_coords = df[['latitude', 'longitude']].values.tolist()
folium.PolyLine(route_coords, color="red", weight=3, opacity=0.8).add_to(m)

# Sla kaart op (verander naam)
m.save("4_VisueleRoutekaart.html")
print("Routekaart opgeslagen als '4_VisueleRoutekaart.html'")
