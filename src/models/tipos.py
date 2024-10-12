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

    def obtener_tipos():
        tipos = session.query(Tipos).join(Categorias).all()
        return tipos
        
    def agregar_tipos():
        tipo = session.add(tipo)
        session.commit()
        return tipo