from fastapi import FastAPI

app = FastAPI()

@app.route("/")
def home():
    return {"message": "starter pack"}

