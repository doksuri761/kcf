import fastapi

responses = fastapi.responses

app = fastapi.FastAPI()


@app.get("/")
def index():
    return responses.JSONResponse({"Test": "Successful"})
