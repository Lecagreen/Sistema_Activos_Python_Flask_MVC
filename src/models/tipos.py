from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base
from src.models.categorias import Categorias 

class Tipos(Base):
    __tablename__ = 'tipos'
    idTipo = Column(Integer, primary_key=True)
    tipo = Column(String(20), nullable=True)
    categoria = Column(Integer, ForeignKey('categorias.idCategoria'), nullable=False)

    def __init__(self, tipo, categoria):
        self.tipo = tipo
        self.categoria = categoria

    def obtener_tipos_activo():
        tipos = session.query(Tipos).all()
        print(tipos)
        return tipos

    def obtener_tipos():
        tipos = session.query(Tipos, Categorias).join(Categorias, Tipos.categoria == Categorias.idCategoria ).all()
        print(Tipos)
        return tipos
        
    def agregar_tipo(tipo):
        tipo = session.add(tipo)
        session.commit()
        return tipo