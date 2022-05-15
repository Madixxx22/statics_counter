import sqlalchemy

from .base import database
from app.models.statics import statics
from app.schemas.statics import Static

class StaticCRUD():
    async def add_static(self, static: Static):
        query = statics.insert().values(date = static.date,
            views = static.views, clicks = static.clicks, cost = static.cost)

        return await database.execute(query)

static_crud = StaticCRUD()