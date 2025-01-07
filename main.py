from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/", response_class=JSONResponse)
async def root():
    foo = {
        "my_first_metric": 25
    }
    return foo
