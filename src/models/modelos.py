from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base
from src.models.marcas import Marcas

class Modelos(Base):
    __tablename__ = 'modelos'
    idModelo = Column(Integer, primary_key=True)
    modelo = Column(String(20), nullable=False)
    marca = Column(Integer, ForeignKey('marcas.idMarca'), nullable=False)

    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca

    def obtener_modelos_activo():
        modelos = session.query(Modelos).all()
        print(modelos)
        return modelos

    def obtener_modelos():
        modelos = session.query(Modelos, Marcas).join(Marcas, Modelos.marca == Marcas.idMarca).all()
        return modelos
        
    def agregar_modelo(modelo):
        modelo = session.add(modelo)
        session.commit()
        return modelo