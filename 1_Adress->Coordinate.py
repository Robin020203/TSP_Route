import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from tqdm import tqdm


# Bestand inlezen
df = pd.read_csv("/Users/robinschildermans/Downloads/Zone7_met_volledige_adressen.csv")

# 1. Adresvelden (zonder BUS) combineren
# Gecombineerde rij = [Straat + huisnummer], [postcode], [gemeente], Belgium
def combine_address(row):
    return f"{row['straat + huisnummer']}, {row['POSTCODE']} {row['GEMEENTE']}, Belgium"

df["volledig_adres"] = df.apply(combine_address, axis=1)

# 2. Nominatim geocoder initialiseren
geolocator = Nominatim(user_agent="postbode_route_planner")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# 3. Coördinaten (latitude/longitude) van volledige adressen geocoderen
latitudes = []
longitudes = []

for adres in tqdm(df["volledig_adres"]):
    try:
        locatie = geocode(adres)
        if locatie:
            latitudes.append(locatie.latitude)
            longitudes.append(locatie.longitude)
        else:
            latitudes.append(None)
            longitudes.append(None)
    except Exception as e:
        print(f"Fout bij '{adres}': {e}")
        latitudes.append(None)
        longitudes.append(None)

# 4. Resultaten toevoegen aan DataFrame
df["latitude"] = latitudes
df["longitude"] = longitudes

# 5. Resultaten opslaan
df.to_csv("1_Zone7_met_coordinaten.csv", index=False)
print("Voltooid! Bestand opgeslagen als '1_Zone7_met_coordinaten.csv'")
