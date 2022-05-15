from fastapi import FastAPI 

from app.db.base import database
from app.schemas.statics import Static
from app.db.static_crud import static_crud
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect() 

@app.post("/save_statics")
async def test(static: Static):
    return await static_crud.add_static(static)