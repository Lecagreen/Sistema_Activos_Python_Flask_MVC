from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from src.models import session, Base
from sqlalchemy_serializer import SerializerMixin
from src.models.empleados import Empleados
from src.models.activos import Activos

class Asignaciones(Base, SerializerMixin):
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
        try:
            asignaciones = session.query(Asignaciones, Empleados, Activos) \
                                  .join(Empleados, Asignaciones.empleado == Empleados.idEmpleado) \
                                  .join(Activos, Asignaciones.activo == Activos.idActivo).all()              
            return asignaciones
        except Exception as e:
            return []
    
    def obtener_asignacion_por_id(idAsignacion):
        try:
            asignacion = session.query(Asignaciones, Empleados, Activos) \
                                .join(Empleados, Asignaciones.empleado == Empleados.idEmpleado) \
                                .join(Activos, Asignaciones.activo == Activos.idActivo) \
                                .filter(Asignaciones.idAsignacion == idAsignacion) \
                                .first()
            return asignacion
        except Exception as e:
            print(f"Error al obtener asignacion por ID {idAsignacion}: {e}")
            return None

    def agregar_asignacion(asignacion):
        asignacion = session.add(asignacion)        
        session.commit()
        return asignacion
    
    @staticmethod
    def editar_asignacion(asignacion):
        asignacion_actual = session.query(Asignaciones).get(asignacion.idAsignacion)
        asignacion_actual.empleado=asignacion.empleado
        asignacion_actual.activo=asignacion.activo
        session.merge(asignacion)
        session.commit()
        return asignacion