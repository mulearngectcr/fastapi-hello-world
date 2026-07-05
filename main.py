from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home(): 
    return {
        "message" : "Hello World"
    }

@app.get("/about")
def aboutme():
    return {
        "name" : "Nandana Sasikumar",
        "bio" : "A developer making her way through 'why does this even work?'"
    }

@app.get("/greet/{name}")
def greeting(name: str):
    return {
        "greet" : f"Hey {name} !!"
    }
