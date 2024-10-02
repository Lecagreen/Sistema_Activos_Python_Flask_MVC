from sqlalchemy import Column, Integer, String, Float, ForeingKey

class Activo():
    _tablename_ = 'activos'

    idActivo = Column(Integer, primary_key=True)
    codigo = Column(Integer)
    tipoActivo = Column(String(20), nullable=False)
    categoriaActivo = Column(String(20), nullable=False)
    descripcion = Column(String(100), nullable=False)
    marca = Column(String(20), ForeingKey('nombre.marca'), nullable=False)
    modelo = Column(String(20), ForeingKey('nombre.modelo'), nullable=False)
    serial = Column(String(20), unique=True, nullable=False)
    largo = Column(Float(10,2))
    ancho = Column(Float(10,2))
    alto = Column(Float(10,2))
    diametro = Column(Float(10,2))
    idUbicacion = Column(Integer, ForeingKey('ubicacion.idubicacion'))

    ubicacion = relationship("Ubicacion", back_populates="activos")