from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy import relationship
from src.models import session, Base

class Activo(Base):
    __tablename__ = 'activos'

    idActivo = Column(Integer, primary_key=True)
    codigo = Column(Integer)
    tipoActivo = Column(String(20), nullable=False)
    categoriaActivo = Column(String(20), nullable=False)
    caracteristicas = Column(String(100), nullable=False)
    marca = Column(String(20), ForeignKey('marca.marca'), nullable=False)
    modelo = Column(String(20), ForeignKey('modelo.modelo'), nullable=False)
    serial = Column(String(20), unique=True, nullable=False)
    largo = Column(Float(10,2))
    ancho = Column(Float(10,2))
    alto = Column(Float(10,2))
    diametro = Column(Float(10,2))
    idUbicacion = Column(Integer, ForeignKey('ubicacion.idubicacion'), nullable=False)

    ubicacion = relationship("Ubicacion", back_populates="activos")

    def __init__(self, codigo, tipoActivo, categoriaActivo, caracteristicas, marca, modelo, serial, largo, ancho, alto, diametro, idUbicacion) -> None:
        self.codigo = codigo
        self.tipoActivo = tipoActivo
        self.categoriaActivo = categoriaActivo
        self.caracteristicas = caracteristicas
        self.marca = marca
        self.modelo = modelo
        self.serial = serial
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.diametro = diametro
        self.idUbicacion = idUbicacion