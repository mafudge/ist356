from fastapi import FastAPI, Body, HTTPException
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv")
app = FastAPI()


@app.get("/api/flights//search")
def search_flights(type: str, code: str):
    '''
    Search for flights by origin and destination
    '''
    if type == "dep":
        flights = df[df["departure_airport_code"] == code]
    elif type == "arr":
        flights = df[df["arrival_airport_code"] == code]
    else:
        raise HTTPException(status_code=400, detail="Invalid type. Must be 'dep' or 'arr'")
    
    return flights.to_dict(orient="records")