import fastapi

responses = fastapi.responses

app = fastapi.FastAPI()


@app.get("/")
def test():
    return responses.JSONResponse({"Test": "Successful"})
