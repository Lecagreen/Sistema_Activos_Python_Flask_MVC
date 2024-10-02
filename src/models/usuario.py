from sqlalchemy import Column, Integer, String, Float, ForeingKey

class Usuario():
    _tablename_ = 'usuario'

    idUsuario = Colum(Integer, primary_key=True)
    usuarioAdv = Column(String(10), unique=True, nullable=True)
    nombres = Column(String(50), nullable=True)
    apellidos = Column(String(50), nullable=True)
    fechaCreacion = Column(Date, nullable=True)
    correoElectronico = Column(String(20), unique=True, nullable=True)
    divisionUsuario = Column(String)