# fastparams.py

from fastapi import FastAPI, Header, Query

app = FastAPI()

@app.get("/calculator/{operator}")  # <== path parameter
def read_item(operator: str, 
              a: float = Query(),     # <== query parameter
              b: float = Query(),     # <== query parameter
              h: str = Header()):     # <== header parameter
    if operator == "add":
        result = a + b
    elif operator == "sub":
        result = a - b
    elif operator == "mul":
        result = a * b
    elif operator == "div":
        result = a / b
    return {
        "operator": operator,
        "a": a,
        "b": b,
        "result": result,
        "h": h
    }