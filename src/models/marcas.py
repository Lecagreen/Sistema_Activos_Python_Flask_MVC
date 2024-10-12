from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Marcas(Base):
    __tablename__ = 'marcas'

    idMarca = Column(Integer, primary_key=True)
    marca = Column(String(20), nullable=True)

    def __init__(self, marca):
        self.marca = marca

    def obtener_marcas():
        marcas = session.query(Marcas).all()
        return marcas
        
    def agregar_marcas():
        marca = session.add(marca)
        session.commit()
        return marca