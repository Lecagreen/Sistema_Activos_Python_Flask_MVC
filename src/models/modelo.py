from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy import relationship
from src.models import session, Base

class Modelo(Base):
    __tablename__ = 'modelo'

    idModelo = Column(Integer, primary_key=True)
    idMarca = Column(Integer, ForeignKey('marca.idMarca'))
    modelo = Column(String(10))

    marca = relationship("Marca", back_populates="modelos")

    def __init__(self, modelo):
        self.modelo = modelo