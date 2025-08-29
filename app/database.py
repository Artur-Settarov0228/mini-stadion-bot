from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base

from .config import config


url = URL.create(
    drivername='sqlpostgres+psycopy2',
    host=config.DB_HOST,
    port=config.DB_PORT,
    username=config.DB_USER,
    database=config.DB_NAME,
    password=config.DB_PASSWORD

)

engine = create_engine(url)