from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy import relationship
from src.models import session, Base

class Ubicacion():

    _tablename_ = 'ubicacion'

    idUbicacion = Column(Integer, primary_key=True)
    ubicacion = Column(String(20))

    activos = relationship("Activo", back_populates="ubicacion")

    def __init__(self, ubicacion):
        self.ubicacion = ubicacion