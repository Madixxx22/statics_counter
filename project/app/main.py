from fastapi import FastAPI 

from app.db.base import database
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect() 

@app.get("/")
async def test():
    return {"result": "access"}