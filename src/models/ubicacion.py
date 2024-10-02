from sqlalchemy import Column, Integer, String, Float, ForeingKey

class Ubicacion():

    _tablename_ = 'ubicacion'

    idUbicacion = Column(Integer, primary_key=True)
    nombreUbicacion = Column(String(20))

    activos = relationship("Activo", back_popuñlates="ubicacion")