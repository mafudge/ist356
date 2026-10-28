import requests

def geocode(location):
    # Call the geocode endpoint; count=1 since we only need the best match
    url = "https://portal.app.cent-su.org/api/weather/geocode"
    params = {"language": "en", "count": 1, "place": location}
    headers = {"accept": "application/json", "X-API-KEY": "cc18c51ef0f3e57e0079d4c5"}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    results = response.json().get("results")
    if not results:
        return None, None
    return results[0]["latitude"], results[0]["longitude"]

if __name__ == "__main__":
    lat, lon = geocode("Syracuse, NY")
    print(lat, lon)
