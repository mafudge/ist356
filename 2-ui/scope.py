name = "mike" # global scope

def setname():
    global name
    name = "john" # I changed global variable in local scope


print(name) # mike
setname()
print(name) # join
