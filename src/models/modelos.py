from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from src.models import session, Base
from src.models.marcas import Marcas

class Modelos(Base):
    __tablename__ = 'modelos'
    idModelo = Column(Integer, primary_key=True)
    modelo = Column(String(20), nullable=False)
    marca = Column(Integer, ForeignKey('marcas.idMarca'), nullable=False)
    estado = Column(Enum('SI', 'NO', name='estado_enum'), default='SI', nullable=False)


    def __init__(self, modelo, marca, estado='SI'):
        self.modelo = modelo
        self.marca = marca
        self.estado = estado

    def obtener_modelos_activo():
        modelos = session.query(Modelos).all()
        print(modelos)
        return modelos
    
    @staticmethod
    def obtener_modelo_por_id(idModelo):
        return session.query(Modelos).filter(Modelos.idModelo == idModelo).first()

    def obtener_modelos():
        modelos = session.query(Modelos, Marcas).join(Marcas, Modelos.marca == Marcas.idMarca).all()
        return modelos
        
    def agregar_modelo(modelo):
        modelo = session.add(modelo)
        session.commit()
        return modelo
    
    def editar_modelo(modelo):
        modelo = session.merge(modelo)
        session.commit()
        return modelo
    
    @staticmethod
    def eliminar_modelo(idModelo):
        modelo = session.query(Modelos).filter(Modelos.idModelo == idModelo).first()
        if modelo:
            modelo.estado = 'NO'
            session.commit()
        return modelo