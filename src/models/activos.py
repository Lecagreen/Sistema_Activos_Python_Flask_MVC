from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base
from src.models.marcas import Marcas
from src.models.modelos import Modelos
from src.models.divisiones import Divisiones
from src.models.categorias import Categorias
from src.models.tipos import Tipos
from src.models.divisiones import Divisiones
from sqlalchemy_serializer import SerializerMixin

class Activos(Base, SerializerMixin):
    __tablename__ = 'activos'
    idActivo = Column(Integer, primary_key=True)
    codigo = Column(Integer, unique=True, nullable=False)
    categoria = Column(Integer, ForeignKey('categorias.idCategoria'), nullable=False)
    tipo = Column(Integer, ForeignKey('tipos.idTipo'), nullable=False)
    caracteristicas = Column(String(100), nullable=False)
    marca = Column(Integer, ForeignKey('marcas.idMarca'))
    modelo = Column(Integer, ForeignKey('modelos.idModelo'))
    serial = Column(String(20), unique=True)
    largo = Column(Float(10,2))
    ancho = Column(Float(10,2))
    alto = Column(Float(10,2))
    diametro = Column(Float(10,2))
    division = Column(Integer, ForeignKey('divisiones.idDivision'), nullable=False)

    def __init__(self, codigo, categoria, tipo, caracteristicas, marca, modelo, serial, largo, ancho, alto, diametro, division):
        self.codigo = codigo
        self.categoria = categoria
        self.tipo = tipo
        self.caracteristicas = caracteristicas
        self.marca = marca
        self.modelo = modelo
        self.serial = serial
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.diametro = diametro
        self.division = division
  
    def obtener_activos():
        try:
            activos = session.query(Activos).join(Marcas).join(Modelos).join(Divisiones).join(Categorias).join(Tipos).all()

            if not activos:
                print("No hay activos disponibles.")
                return []

            print(activos[0].to_dict())
            return activos
        except Exception as e:
            print(f"Error al obtener activos: {e}")
            return []
        
    def agregar_activo(activo):
        activo = session.add(activo)
        session.commit()
        return activo
    
    def to_dict_custom(self):

        return {
            'categoria': self.categoria,
            'tipo': self.tipo,
            'caracteristicas': self.caracteristicas,
            'division': self.division 
        }

    @staticmethod
    def obtener_activo_por_id(idActivo):
        try:
            activo = session.query(Activos).filter_by(idActivo=idActivo).first()
            return activo.to_dict_custom() if activo else None
        except Exception as e:
            print(f"Error al obtener activo por ID {idActivo}: {e}")
            return None