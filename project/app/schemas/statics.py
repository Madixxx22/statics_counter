import datetime
from decimal import Decimal
from pydantic import BaseModel, validator


class StaticBase(BaseModel):
    date: datetime.date = datetime.date.today()
    views: int = None
    clicks: int = None
    cost: Decimal = None

    @classmethod
    def check_value(cls, views):
        if views < 0:
            raise ValueError("views, clicks or cost negative!")
        return views

    @validator("views")
    def check_views(cls, views):
        return cls.check_value(views)
    
    @validator("clicks")
    def check_clicks(cls, clicks):
        return cls.check_value(clicks)

    @validator("cost")
    def check_cost(cls, cost):
        return cls.check_value(cost)


class Static(StaticBase):
    pass

class GetStatic(BaseModel):
    from_date: datetime.date
    to_date: datetime.date


class RequestStatic(StaticBase):
    cpc: Decimal
    cpm: Decimal