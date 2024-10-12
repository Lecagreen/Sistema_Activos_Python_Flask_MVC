from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base
from src.models.marcas import Marcas

class Modelos(Base):
    __tablename__ = 'modelos'

    idModelo = Column(Integer, primary_key=True)
    modelo = Column(String(10))
    marca = Column(Integer, ForeignKey('marcas.idMarca'))

    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca

    def obtener_modelos():
        modelos = session.query(Modelos).join(Marcas).all()
        return modelos
        
    def agregar_modelos():
        modelo = session.add(modelo)
        session.commit()
        return modelo