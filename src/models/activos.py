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
    categoria_id = Column(Integer, ForeignKey('categorias.idCategoria'), nullable=False)
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

    def __init__(self, codigo, categoria_id, tipo, caracteristicas, marca, modelo, serial, largo, ancho, alto, diametro, division):
        self.codigo = codigo
        self.categoria_id = categoria_id
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
        activos = session.query(Activos, Categorias, Tipos, Marcas, Modelos, Divisiones) \
                         .join(Categorias, Activos.categoria_id == Categorias.idCategoria) \
                         .join(Tipos, Activos.tipo == Tipos.idTipo) \
                         .join(Marcas, Activos.marca == Marcas.idMarca) \
                         .join(Modelos, Activos.modelo == Modelos.idModelo) \
                         .join(Divisiones, Activos.division == Divisiones.idDivision).all()
        print(activos)
        return activos
    
    @staticmethod
    def obtener_activos_asignacion():
        activos = session.query(Activos).all()
        return activos
        
    def agregar_activo(activo):
        activo = session.add(activo)
        session.commit()
        return activo

    @staticmethod
    def obtener_activo_por_id(idActivo):
        try:
            activo = (
                session.query(Activos,Categorias, Tipos, Divisiones)
                .join(Categorias,Activos.categoria_id == Categorias.idCategoria)
                .join(Tipos,Activos.tipo == Tipos.idTipo)
                .join(Divisiones, Activos.division == Divisiones.idDivision)
                .filter(Activos.idActivo == idActivo)
                .first()
            )
            if activo:
                activo_info, categoria_info, tipo_info, division_info = activo
                return {
                    'idActivo': activo_info.idActivo,
                    'categoriaActivo': categoria_info.categoria,
                    'tipoActivo': tipo_info.tipo,
                    'caracteristicas': activo_info.caracteristicas,
                    'divisionActivo': division_info.division
                }
            else:
                return None
        except Exception as e:
            print(f"Error al obtener activo por ID {idActivo}: {e}")
            return None