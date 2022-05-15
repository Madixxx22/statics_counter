from fastapi import FastAPI 

from app.db.base import database
from app.db.static_crud import static_crud
from app.schemas.statics import CriteriaStatic, Static, StaticDB


app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect() 

@app.post("/save-statics")
async def save_statics(static: Static):
    static_in_db = StaticDB(**static.dict(), cpc=(static.cost / static.clicks), cpm=(static.cost / static.clicks * 1000))
    return await static_crud.add_static(static_in_db)

@app.post("/read-staticks")
async def read_statics(criteria: CriteriaStatic):
    static_db = await static_crud.get_statics(criteria)
    return static_db

@app.delete("/reset-statics")
async def reset_statics():
    return await static_crud.reset_statics()