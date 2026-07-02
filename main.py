from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def message():
    return {"message": "Hello from my API"}

@app.get('/about')
def intro():
    return {"Name": "Sooraj K R", "Bio": "Hi i am a 3rd year CSE student who is constantly learning"}

@app.get('/greet/{name}')
def greet(name: str):
    return {"message": f"Hello {name}, nice to meet you"}
