from fastapi import FastAPI, Header, Body, Query, HTTPException

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello World"}

@app.get("/hello/uri/{name}")
def hello_uri(name: str):
    return {"message": f"Hello World, {name}"}

@app.get("/hello/querystr")
def hello_querystr(name: str, age: int=99):
    return {"message": f"Hello {name}, you are {age} years old."}

@app.get("/hello/header")
def hello_header(name: str = Header(), age: int = Header(99)):
    return {"message": f"Hello {name}, you are {age} years old."}

@app.post("/hello/post")
def hello_post(name: str = Body(), age: int = Body(99)):
    return {"message": f"Hello {name}, you are {age} years old."}


@app.post("/hello/full/{name}")
def hello_full(name: str, age: int = Query(99), x_api_key: str = Header(),  email: str= Body(), phone: str = Body()):
    if x_api_key != "secret":
        raise HTTPException(status_code=401, detail = {"message": "Invalid API Key"})
    
    return {"message": { 
        "name": name,
        "email" :email,
        "phone": phone,
        "age" : age}
     } 