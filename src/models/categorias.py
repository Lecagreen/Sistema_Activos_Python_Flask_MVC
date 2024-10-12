from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Categorias(Base):
    __tablename__ = 'categorias'

    idCategoria = Column(Integer, primary_key=True)
    categoria = Column(String(20), nullable=True)

    def __init__(self, categoria):
        self.categoria = categoria

    def obtener_categorias():
        categorias = session.query(Categorias).all()
        return categorias
        
    def agregar_categorias():
        categoria = session.add(categoria)
        session.commit()
        return categoria