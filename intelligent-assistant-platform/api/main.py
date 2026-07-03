from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Fast API is running!"}