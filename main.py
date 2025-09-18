import datetime

from fastapi import FastAPI

app = FastAPI(
    title="Example API",
    version="0.2.2",
)

@app.get("/hello")
async def hello_world():
    return {
        "message": "Hello, world!",
        "timestamp": str(datetime.datetime.now(datetime.timezone.utc)),
        "version": app.version,
    }
