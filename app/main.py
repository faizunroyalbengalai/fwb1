from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

app = FastAPI(title="fwb1", version="1.0.0")

from app.routers import health, api

app.include_router(health.router)
app.include_router(api.router)


@app.get("/")
async def root():
    return JSONResponse(content={"message": "Python App is running", "app": "fwb1", "status": "ok"})


if __name__ == "__main__":
    import uvicorn
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run("app.main:app", host=host, port=port, reload=False)