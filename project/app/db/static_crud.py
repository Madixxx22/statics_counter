import sqlalchemy

from .base import database
from app.models.statics import statics
from app.schemas.statics import CriteriaStatic, Static, StaticDB

class StaticCRUD():

    async def add_static(self, static: Static):
        query = statics.insert().values(date = static.date, views = static.views,
            clicks = static.clicks, cost = static.cost, cpc = static.cpc, cpm = static.cpm)
        return await database.execute(query)

    async def get_statics(self, criteria: CriteriaStatic):
        if criteria.name_column_sorted == "":
            if criteria.sorting_from_last == True:
                query = statics.select().where((statics.c.date >= criteria.from_date),
                    (statics.c.date <= criteria.to_date)).order_by(sqlalchemy.desc(statics.c.date))
            else:
                query = statics.select().where((statics.c.date >= criteria.from_date),
                    (statics.c.date <= criteria.to_date)).order_by(statics.c.date)

        else:
            if criteria.sorting_from_last == True:
                query = f'''SELECT *
                            FROM statics
                            WHERE '{criteria.from_date}' <= statics.date AND statics.date <= '{criteria.to_date}'
                            ORDER BY statics.date DESC, statics.{criteria.name_column_sorted}'''
            else:
                query = f'''SELECT *
                            FROM statics
                            WHERE '{criteria.from_date}' <= statics.date AND statics.date <= '{criteria.to_date}'
                            ORDER BY statics.date, statics.{criteria.name_column_sorted}'''

        return await database.fetch_all(query)

static_crud = StaticCRUD()