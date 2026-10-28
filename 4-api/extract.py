import os
import requests
import json

def extract_entities( text: str) -> list[dict]:

    CENT_API_KEY = os.getenv("CENT_API_KEY")

    # building the prompt
    PROMPT_TEMPLATE = """
    Extract Entities from this text:

    I expect the following:

    "text" => the text extracted
    "type" => a classification of the text extracted ex. Place
    "subtype" => a further classificatino of the text extracted ex. Baseball Stadium"
    "justification" => your reasoning as to why it is classified they way it is.
    "explanation" => explain in detail the classification 

    Output in JSON format:
    ```JSON
    [ 
        {"text" : "McDonalds", "type" :"Restaraunt", "subtype" : "Fast Food", "explanation": "This is a fast food restaraunt.", "justification" : "I am aware that McDonalds is a fast-food restaraunt" },
        {"text" : "Gradma Carol", "type" :"Person", "subtype" : "Relative", "explanation": "This is someone's grandparent", "justification" : "Gradma is a term for someone's relative." }
    ]
    ```
    Always and only output a JSON array of objects with the following keys: 
    text, type, subtype, explanation, justification. Do not output any other text.

    <TEXT>
    {input_text}
    """

    input_text = text 
    prompt = PROMPT_TEMPLATE.replace("{input_text}", input_text)

    #setup the API request
    url = "https://portal.app.cent-su.org/api/azure/foundry/generate"

    params = {
        "model": "gpt-6-luna",
        "max_tokens": 2000,
        "reasoning_effort": "low",
        "cache": "false",
    }

    headers = {
        "accept": "application/json",
        "X-API-KEY": CENT_API_KEY,
        # requests sets Content-Type automatically for data=dict, but it's explicit here to match the curl call
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "query": prompt,
    }

    # call the api 
    response = requests.post(url, params=params, headers=headers, data=data)
    response.raise_for_status()  # raises requests.exceptions.HTTPError on 4xx/5xx


    # this might be mike's Iot Portal API problem
    data = response.json()  # deserialize the response
    if isinstance(data, str):
        data = json.loads(data)

    return data

if __name__ == "__main__":
    import dotenv
    dotenv.load_dotenv()
    text = "New York City is awesome."
    entities = extract_entities(text)
    print(entities)
    assert entities[0]["text"] == "New York City"
    assert entities[0]["type"] is not None
    assert entities[0]["subtype"] is not None

