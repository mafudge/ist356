from fastapi import FastAPI, Body

app = FastAPI()

friends = []  # global variable to store the list of friends

@app.post("/friends")
def create_friend(name: str = Body(), age: int = Body()):
    '''
    Add a new friend to the list of friends and return the list each time a new friend is added
    ''' 
    friend = {"name": name, "age": age}
    friends.append(friend)
    return friends