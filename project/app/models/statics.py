import sqlalchemy

from app.db.base import metadata

statics = sqlalchemy.Table(
    'statics',
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column("date", sqlalchemy.Date()),
    sqlalchemy.Column("views", sqlalchemy.Integer()),
    sqlalchemy.Column("clicks", sqlalchemy.Integer()),
    sqlalchemy.Column("cost", sqlalchemy.Numeric())
    )