import requests
import pandas as pd
# uri = "https://portal.app.cent-su.org/api/funnyname/random?n=5"
# response = requests.get(uri)
# # deserialize the response to a Python object
# response.raise_for_status() # thow an exception if the request failed
# data = response.json() #parses for you!
# for name in data:
#     print(name['first'], name['last'])

url = "https://portal.app.cent-su.org/api/weather/geocode"
params = {
    "language": "en",
    "count": 2,
    "place": "Syracuse, New York",
}
headers = {
    "accept": "application/json",
    "X-API-KEY": "0f92bf60ff8c50f7e6929e57",
}

response = requests.get(url, params=params, 
                        headers=headers, timeout=30)
print(response.url)
response.raise_for_status()

data = response.json()
df = pd.json_normalize(data['results'])
print(df)
 
