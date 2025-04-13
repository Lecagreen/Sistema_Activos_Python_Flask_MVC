from sqlalchemy import Column, Integer, String, Enum, create_engine
from src.models import session, Base

class Marcas(Base):
    __tablename__ = 'marcas'

    idMarca = Column(Integer, primary_key=True)
    marca = Column(String(20),unique=True, nullable=True)
    estado = Column(Enum('SI', 'NO', name='estado_enum'), default='SI', nullable=False)

    def __init__(self, marca, estado='SI'):
        self.marca = marca
        self.estado = estado

    def to_dict(self):

        return {
            'idMarca': self.idMarca,
            'marca': self.marca,
            'estado' : self.estado
    }

    def obtener_marcas():
        marcas = session.query(Marcas).all()
        return marcas
    
    @staticmethod
    def obtener_marca_por_id(idMarca):
        return session.query(Marcas).filter(Marcas.idMarca == idMarca).first()
        
    def agregar_marca(marca):
        marca = session.add(marca)
        session.commit()
        return marca
    
    @staticmethod
    def editar_marca(marca):
        session.merge(marca)
        session.commit()
        return marca

    @staticmethod
    def eliminar_marca(idMarca):
        marca = session.query(Marcas).filter(Marcas.idMarca == idMarca).first()
        if marca:
            marca.estado = 'NO'
            session.commit()
        return marca