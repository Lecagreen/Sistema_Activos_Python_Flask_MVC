from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Ubicaciones(Base):
    __tablename__ = 'ubicaciones'
    idUbicacion = Column(Integer, primary_key=True)
    ubicacion = Column(String(20), nullable=True)
    piso = Column(String(20))
    puesto = Column(String(20))

    def __init__(self, ubicacion, piso, puesto):
        self.ubicacion = ubicacion
        self.piso = piso
        self.puesto = puesto

    def obtener_ubicaciones():
        ubicaciones = session.query(Ubicaciones).all()
        return ubicaciones
    
    @staticmethod
    def obtener_ubicacion_por_id(idUbicacion):
        return session.query(Ubicaciones).filter(Ubicaciones.idUbicacion == idUbicacion).first()
        
    def agregar_ubicacion(ubicacion):
        ubicacion = session.add(ubicacion)
        session.commit()
        return ubicacion
    
    @staticmethod
    def editar_ubicacion(ubicacion):
        session.merge(ubicacion)
        session.commit()
        return ubicacion