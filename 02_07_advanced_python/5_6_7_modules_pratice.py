import pickle
import json
import re

data = {"name": "Alice", "age": 25}

def printPickle():
    with open("data.pkl", "wb") as f:
        unload = pickle.dump(data, f)

    with open("data.pkl", "rb") as f:
        loaded = pickle.load(f)
        print(loaded)

def printJson():
    with open("data.json", "w") as f:
        json.dump(data, f)

    with open("data.json", "r") as f:
        loaded_json = json.load(f)
        print(loaded_json)

def checkValidEmail():
    email = "test@example.com"
    if re.findall(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        print("Valid email")
    else:
        print("Invalid email")


printPickle()
printJson()
checkValidEmail()




