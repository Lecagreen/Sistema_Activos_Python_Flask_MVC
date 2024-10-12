from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Divisiones(Base):
    __tablename__ = 'divisiones'

    idDivision = Column(Integer, primary_key=True)
    division = Column(String(20), nullable=True)

    def __init__(self, division):
        self.division = division

    def obtener_divisiones():
        divisiones = session.query(Divisiones).all()
        return divisiones
        
    def agregar_divisiones():
        division = session.add(division)
        session.commit()
        return division