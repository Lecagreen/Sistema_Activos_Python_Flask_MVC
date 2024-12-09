from sqlalchemy import Column, Integer, String, Enum
from src.models import session, Base

class Ubicaciones(Base):
    __tablename__ = 'ubicaciones'
    idUbicacion = Column(Integer, primary_key=True)
    ubicacion = Column(String(20), nullable=True)
    piso = Column(String(20))
    puesto = Column(String(20))
    estado = Column(Enum('SI', 'NO', name='estado_enum'), default='SI', nullable=False) 

    def __init__(self, ubicacion, piso, puesto, estado='SI'):
        self.ubicacion = ubicacion
        self.piso = piso
        self.puesto = puesto
        self.estado = estado

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
    
    @staticmethod
    def eliminar_ubicacion(idUbicacion):
        ubicacion = session.query(Ubicaciones).filter(Ubicaciones.idUbicacion == idUbicacion).first()
        if ubicacion:
            ubicacion.estado = 'NO'
            session.commit()
        return ubicacion