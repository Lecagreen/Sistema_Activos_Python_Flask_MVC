from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Ubicaciones(Base):
    __tablename__ = 'ubicaciones'

    idUbicacion = Column(Integer, primary_key=True)
    ubicacion = Column(String(20))

    def __init__(self, ubicacion):
        self.ubicacion = ubicacion

    def obtener_ubicaciones():
        ubicaciones = session.query(Ubicaciones).all()
        return ubicaciones
        
    def agregar_ubicaciones():
        ubicacion = session.add(ubicacion)
        session.commit()
        return ubicacion