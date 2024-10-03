from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from src.models import session, Base

class Usuario():
    _tablename_ = 'usuario'

    idUsuario = Column(Integer, primary_key=True)
    usuarioAdv = Column(String(10), unique=True, nullable=True)
    nombres = Column(String(50), nullable=True)
    apellidos = Column(String(50), nullable=True)
    fechaCreacion = Column(Date, nullable=True)
    correoElectronico = Column(String(20), unique=True, nullable=True)
    division = Column(String, ForeignKey('division.division'), nullable=False)

    def __init__(self, usuarioAdv, nombres, apellidos, fechaCreacion, correoElectronico, division):
        self.usuarioAdv = usuarioAdv
        self.nombres = nombres
        self.apellidos = apellidos
        self.fechaCreacion = fechaCreacion
        self.correoElectronico = correoElectronico
        self.division = division