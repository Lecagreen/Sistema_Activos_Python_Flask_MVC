from flask_sqlalchemy import SQLAlchemy
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:123456@localhost:5432/control_activos")

connection = engine.connect

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)

session = Session()
