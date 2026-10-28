import requests
import streamlit as st
import dotenv
import os

dotenv.load_dotenv()
CENT_API_KEY = os.getenv("CENT_API_KEY")

# Build prompt
PROMPT_TEMPLATE = '''
Perform entity extraction on <TEXT>. For each entity label its kind (person, place, event, etc) and try to label a sub-kind (city, currency, type of food)

Output in JSON format so I can read it with code. For example:

```JSON
[ 
 { "text" : "New York City".
    "kind" : "Location",
    "Sub-Kind" : "City",
    "Info" : "This is a US city"
}
]
```

<TEXT> {text_input}
'''
text_input = "IST356 is probably the worst college course I've ever taken. Professor Fudge is a total tool."

prompt = PROMPT_TEMPLATE.replace("{text_input}", text_input)

# build request
url = "https://portal.app.cent-su.org/api/azure/foundry/generate"

params = {
    "model": "gpt-6-luna",
    "max_tokens": 4000,
    "reasoning_effort": "low",
    "cache": "true",
}

headers = {
    "accept": "application/json",
    "X-API-KEY": CENT_API_KEY,
    "Content-Type": "application/x-www-form-urlencoded",
}

data = {"query": prompt}

# Make the API call
response = requests.post(url, params=params, headers=headers, data=data)
response.raise_for_status()  # raise an exception if the request failed

# deserialize the response
data = response.json()  # python object!!
print(data)
