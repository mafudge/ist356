from fastapi import FastAPI, Body, HTTPException


friends = []
app = FastAPI()

@app.post("/friends")
def create_friend(name: str = Body(), age: int = Body()):
    '''
    Add a new friend to the list of friends and return the list each time a new friend is added
    ''' 
    friend = {"name": name, "age": age}
    friends.append(friend)
    return {"added" : friend }

@app.get("/friends")
def get_friends():
    '''
    Return the list of friends
    '''
    return friends


@app.put("/friends/{name}")
def update_friend(name: str, age: int = Body()):
    '''
    Update the age of a friend
    '''
    for friend in friends:
        if friend["name"] == name:
            friend["age"] = age
            return {"updated": friend}
    raise HTTPException(status_code=404, detail="Friend not found")


@app.delete("/friends/{name}")
def delete_friend(name: str):
    '''
    Delete a friend from the list
    '''
    for friend in friends:
        if friend["name"] == name:
            friends.remove(friend)
            return {"deleted": friend }
    raise HTTPException(status_code=404, detail="Friend not found")