from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Marca(Base):
    __tablename__ = 'marca'

    idMarca = Column(Integer, primary_key=True)
    marca = Column(String(20), nullable=True)

    def __init__(self, marca):
        self.marca = marca