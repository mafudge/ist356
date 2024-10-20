# fastparams2.py

from fastapi import FastAPI, Header, Query, HTTPException

app = FastAPI()

@app.get("/calculator/{operator}")  # <== path parameter
def read_item(operator: str, 
              a: str = Query(),     # <== query parameter
              b: int = Query(),     # <== query parameter
              h: str = Header()):   # <== header parameter
    if operator == "add":
        result = a + b
    elif operator == "sub":
        result = a - b
    elif operator == "mul":
        result = a * b
    elif operator == "div":
        result = a / b
    else:
        raise HTTPException(status_code=404, detail="Operator not found. should be: add, sub, mul, div")
    
    return {
        "operator": operator,
        "a": a,
        "b": b,
        "result": result,
        "h": h
    }