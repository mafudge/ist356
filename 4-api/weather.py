

def geocode(location):
    # Call the geocode endpoint; count=1 since we only need the best match
    url = "https://portal.app.cent-su.org/api/weather/geocode"
    params = {"language": "en", "count": 1, "place": location}
    headers = {"accept": "application/json", "X-API-KEY": CENT_API_KEY}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    results = response.json().get("results")
    if not results:
        return None, None
    return results[0]["latitude"], results[0]["longitude"]

def weather(lat, lon):
    url = "https://portal.app.cent-su.org/api/weather/current"
    params = {"units": "imperial", "lat": lat, "lon": lon}
    headers = {"accept": "application/json", "X-API-KEY": CENT_API_KEY}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()["current"]["temperature_2m"]


if __name__ == "__main__":
    import dotenv
    import os
    import requests

    dotenv.load_dotenv(".env")
    CENT_API_KEY = os.getenv("CENT_API_KEY")

    # smoke test
    lat, lon = geocode("Syracuse, NY")
    temp = weather(lat, lon)
    print(f"Temperature in Syracuse, NY: {temp}°F (lat: {lat}, lon: {lon})")
