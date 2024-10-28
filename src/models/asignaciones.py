from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from src.models import session, Base

class Asignaciones(Base):
    __tablename__ = 'asignaciones'
    idAsignacion = Column(Integer, primary_key=True)
    fecha = Column(DateTime, nullable=False)
    empleado = Column(Integer, ForeignKey('empleados.idEmpleado'), nullable=False)
    activo = Column(Integer, ForeignKey('activos.idActivo'), nullable=False)

    def __init__(self,fecha, empleado, activo):
        self.fecha=fecha
        self.empleado=empleado
        self.activo=activo
        
    def obtener_asignaciones():
        asignaciones = session.query(Asignaciones).all()              
        return asignaciones

    def agregar_asignacion(asignacion):
        asignacion = session.add(asignacion)        
        session.commit()
        return asignacion