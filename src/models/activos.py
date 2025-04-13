from sqlalchemy import Column, Integer, String, ForeignKey
from src.models import session, Base
from src.models.marcas import Marcas
from src.models.modelos import Modelos
from src.models.divisiones import Divisiones
from src.models.categorias import Categorias
from src.models.tipos import Tipos
from sqlalchemy_serializer import SerializerMixin

class Activos(Base, SerializerMixin):
    __tablename__ = 'activos'
    
    idActivo = Column(Integer, primary_key=True)
    codigo = Column(Integer, unique=True, nullable=False)
    categoria = Column(Integer, ForeignKey('categorias.idCategoria'), nullable=False)
    tipo = Column(Integer, ForeignKey('tipos.idTipo'), nullable=False)
    caracteristicas = Column(String(100), nullable=False)
    marca = Column(Integer, ForeignKey('marcas.idMarca'), nullable=True)
    modelo = Column(Integer, ForeignKey('modelos.idModelo'), nullable=True)
    serial = Column(String(20), unique=True, nullable=True)
    largo = Column(String(6), nullable=True)
    ancho = Column(String(6), nullable=True)
    alto = Column(String(6),nullable=True)
    diametro = Column(String(6), nullable=True)
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

    def __repr__(self):
        return f"<Activos(idActivo={self.idActivo}, codigo={self.codigo}, caracteristicas='{self.caracteristicas}', serial='{self.serial}')>"
        
    def to_dict(self):
        return {
            'idActivo': self.idActivo,
            'codigo': self.codigo,
            'categoria': self.categoria,
            'tipo': self.tipo,
            'caracteristicas': self.caracteristicas,
            'marca': self.marca,
            'modelo': self.modelo,
            'serial': self.serial,
            'largo': self.largo,
            'ancho': self.ancho,
            'alto': self.alto,
            'diametro': self.diametro,
            'division': self.division
        }
    
    @staticmethod
    def obtener_activos():
        try:
            activos = session.query(Activos, Categorias, Tipos, Marcas, Modelos, Divisiones) \
                            .join(Categorias, Activos.categoria == Categorias.idCategoria) \
                            .join(Tipos, Activos.tipo == Tipos.idTipo) \
                            .outerjoin(Marcas, Activos.marca == Marcas.idMarca) \
                            .outerjoin(Modelos, Activos.modelo == Modelos.idModelo) \
                            .join(Divisiones, Activos.division == Divisiones.idDivision).all()
            for act in activos:
                print(act)
            return activos
        except Exception as e:
            print(f"Error al obtener activos: {e}")
            return []
        
    def obtener_activos_api():
        try:
            activos = session.query(Activos).all()
            resultado = [activo.to_dict() for activo in activos]
            return resultado
        except Exception as e:
            print(f"Error al obtener activos: {e}")
            return []

    @staticmethod
    def agregar_activo(activo):
        try:
            session.add(activo)
            session.commit()
            return activo
        except Exception as e:
            session.rollback()
            print(f"Error al agregar activo: {e}")
            return None
    
    @staticmethod
    def obtener_activo_por_id(idActivo):
        try:
            activo = (
                session.query(Activos, Categorias, Tipos, Divisiones)
                .join(Categorias, Activos.categoria == Categorias.idCategoria)
                .join(Tipos, Activos.tipo == Tipos.idTipo)
                .join(Marcas, Activos.marca == Marcas.idMarca )
                .join(Modelos, Activos.modelo == Modelos.idModelo)
                .join(Divisiones, Activos.division == Divisiones.idDivision)
                .filter(Activos.idActivo == idActivo)
                .first()
            )
            if activo:
                activo_info, categoria_info, tipo_info, division_info = activo
                return {
                    'idActivo': activo_info.idActivo,
                    'codigo': activo_info.codigo,
                    'categoriaActivo': categoria_info.categoria,
                    'tipoActivo': tipo_info.tipo,
                    'caracteristicas': activo_info.caracteristicas,
                    'marca': activo_info.marca or " ",
                    'modelo': activo_info.modelo or " ",
                    'serial': activo_info.serial or " ",
                    'largo': activo_info.largo or " ",
                    'ancho': activo_info.ancho or " ",
                    'alto': activo_info.alto or " ",
                    'diametro': activo_info.diametro or " ",
                    'divisionActivo': division_info.division
                }
            else:
                return None
        except Exception as e:
            print(f"Error al obtener activo por ID {idActivo}: {e}")
            return None
    
    @staticmethod
    def obtener_activo_asignacion(idActivo):
        try:
            activo = (
                session.query(Activos,Categorias, Tipos, Divisiones)
                .join(Categorias,Activos.categoria == Categorias.idCategoria)
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
        
    @staticmethod
    def obtener_activos_asignacion():
        activos = session.query(Activos).all()
        return activos
        
    @staticmethod
    def editar_activo(activo):
        session.merge(activo)
        session.commit()
        return activo