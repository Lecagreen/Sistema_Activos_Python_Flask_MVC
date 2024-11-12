from sqlalchemy import Column, Integer, String
from src.models import session, Base

class Categorias(Base):
    __tablename__ = 'categorias'
    idCategoria = Column(Integer, primary_key=True)
    categoria = Column(String(30), unique=True, nullable=False)
    
    def __init__(self, categoria):
        self.categoria = categoria

    @staticmethod
    def obtener_categorias():
        categorias = session.query(Categorias).all()
        return categorias

    @staticmethod
    def obtener_categoria_por_id(idCategoria):
        return session.query(Categorias).filter(Categorias.idCategoria == idCategoria).first()

    @staticmethod
    def agregar_categoria(categoria):
        session.add(categoria)
        session.commit()
        return categoria

    @staticmethod
    def editar_categoria(categoria):
        session.merge(categoria)
        session.commit()
        return categoria