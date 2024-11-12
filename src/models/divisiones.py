from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Divisiones(Base):
    __tablename__ = 'divisiones'
    idDivision = Column(Integer, primary_key=True)
    division = Column(String(20), unique=True, nullable=True)

    def __init__(self, division):
        self.division = division

    def obtener_divisiones():
        divisiones = session.query(Divisiones).all()
        return divisiones
    
    @staticmethod
    def obtener_division_por_id(idDivision):
        return session.query(Divisiones).filter(Divisiones.idDivision == idDivision).first()
        
    def agregar_division(division):
        division = session.add(division)
        session.commit()
        return division
    
    @staticmethod
    def editar_division(division):
        session.merge(division)
        session.commit()
        return division