from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from src.models import session, Base
from src.models.categorias import Categorias 

class Tipos(Base):
    __tablename__ = 'tipos'
    idTipo = Column(Integer, primary_key=True)
    tipo = Column(String(20), nullable=True)
    categoria = Column(Integer, ForeignKey('categorias.idCategoria'), nullable=False)
    estado = Column(Enum('SI', 'NO', name='estado_enum'), default='SI', nullable=False)

    def __init__(self, tipo, categoria, estado='SI'):
        self.tipo = tipo
        self.categoria = categoria
        self.estado = estado

    def obtener_tipos_activo():
        tipos = session.query(Tipos).all()
        print(tipos)
        return tipos

    def obtener_tipos():
        tipos = session.query(Tipos, Categorias).join(Categorias, Tipos.categoria == Categorias.idCategoria ).all()
        print(Tipos)
        return tipos
    
    @staticmethod
    def obtener_tipo_por_id(idTipo):
        return session.query(Tipos).filter(Tipos.idTipo == idTipo).first()
        
    def agregar_tipo(tipo):
        tipo = session.add(tipo)
        session.commit()
        return tipo
    
    @staticmethod
    def editar_tipo(tipo):
        session.merge(tipo)
        session.commit()
        return tipo
    
    @staticmethod
    def eliminar_tipo(idTipo):
        tipo = session.query(Tipos).filter(Tipos.idTipo == idTipo).first()
        if tipo:
            tipo.estado = 'NO'
            session.commit()
        return tipo