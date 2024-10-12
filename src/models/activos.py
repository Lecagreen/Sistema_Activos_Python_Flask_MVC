from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base
from src.models.marcas import Marcas
from src.models.modelos import Modelos
from src.models.ubicaciones import Ubicaciones
from src.models.divisiones import Divisiones
from src.models.categorias import Categorias
from src.models.tipos import Tipos

class Activos(Base):
    __tablename__ = 'activos'

    idActivo = Column(Integer, primary_key=True)
    codigo = Column(Integer)
    tipo = Column(Integer, ForeignKey('tipos.idTipo'), nullable=False)
    categoria = Column(Integer, ForeignKey('categorias.idCategoria'), nullable=False)
    caracteristicas = Column(String(100), nullable=False)
    marca = Column(Integer, ForeignKey('marcas.idMarca'), nullable=False)
    modelo = Column(Integer, ForeignKey('modelos.idModelo'), nullable=False)
    serial = Column(String(20), unique=True, nullable=False)
    largo = Column(Float(10,2))
    ancho = Column(Float(10,2))
    alto = Column(Float(10,2))
    diametro = Column(Float(10,2))
    division = Column(Integer, ForeignKey('divisiones.idDivision'), nullable=False)
    ubicacion = Column(Integer, ForeignKey('ubicaciones.idUbicacion'), nullable=False)

    def __init__(self, codigo, tipo, categoria, caracteristicas, marca, modelo, serial, largo, ancho, alto, diametro, ubicacion) -> None:
        self.codigo = codigo
        self.tipo = tipo
        self.categoria = categoria
        self.caracteristicas = caracteristicas
        self.marca = marca
        self.modelo = modelo
        self.serial = serial
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.diametro = diametro
        self.ubicacion = ubicacion

    def obtener_activos():
        activos = session.query(Activos).join(Marcas).join(Modelos).join(Ubicaciones).join(Divisiones).join(Categorias).join(Tipos).all()
        return activos
        
    def agregar_activos():
        activo = session.add(activo)
        session.commit()
        return activo