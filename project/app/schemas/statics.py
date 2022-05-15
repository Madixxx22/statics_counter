import datetime
from decimal import Decimal
from enum import Enum
from pydantic import BaseModel, validator


class StaticBase(BaseModel):
    date: datetime.date = datetime.date.today()
    views: int = 1
    clicks: int = 1
    cost: Decimal = 1

    @classmethod
    def check_value(cls, views):
        if views <= 0:
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

class CriteriaStatic(BaseModel):
    from_date: datetime.date
    to_date: datetime.date
    name_column_sorted: str = " "
    sorting_from_last: bool = True

    @validator("name_column_sorted")
    def check_name_column(cls, name_column):
        if name_column not in ["views", "clicks", "cost", "cpc", "cpm", " "]:
            raise ValueError("A nonexistent column is specified for sorting")
        return name_column


class StaticDB(StaticBase):
    cpc: Decimal
    cpm: Decimal

class ColumnSorted(Enum):
    views = "views"
    clicks = "clicks"
    cost = "cost" 
    cpc = "cpc"
    cpm = "cpm"
    Nothing = " "