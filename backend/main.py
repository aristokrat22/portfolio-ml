from fastapi import FastAPI

app = FastAPI()

@app.get("/api/models/predict-price-house")
def hello():
    return {"message": "Бэк на связи!4Aristokrat44"}


@app.get("/api/models/predict-price-car")
def hello():
    return {"message": "БCARS CARF676767"}


