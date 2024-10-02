from sqlalchemy import Column, Integer, String, Float, ForeingKey

class Modelo():
    _tablename_ = 'modelo'

    idModelo = Column(Integer, primary_key=True)
    idMarca = Column(Integer, ForeingKey('marca.idMarca'))
    nombreMarca = Column(String(10))

    marca = relationship("Marca", back_populates="modelos")