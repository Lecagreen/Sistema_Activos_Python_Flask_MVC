from sqlalchemy import Column, Integer, String, Float, ForeingKey

class Marca():
    _tablename_ = 'marca'

    idMarca = Column(Integer, primary_key=True)
    nombreMarca = Column(Srring(20), nullable=True)