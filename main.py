from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read():
    return {"message": "Hello from my API"}


@app.get("/bio")
def bio():
    return {"message": "My name is Sreelekshmi,I am a student at Govt Engineering College,Thrissur"}

@app.get("/greeting/{name}")
def greeting(name: str):
    return {"message": f"Hello ,{name}!"}