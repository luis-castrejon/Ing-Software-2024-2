from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class Renta(Base):
    __tablename__ = 'rentar'
    
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'), nullable=False)
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'), nullable=False)
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Boolean, default=False)
    fecha_devolucion = Column(DateTime)

    usuario = relationship("Usuario", back_populates="rentas")
    pelicula = relationship("Pelicula", back_populates="rentas")

    def __repr__(self):
        return f"<Renta(idRentar={self.idRentar}, idUsuario={self.idUsuario}, idPelicula={self.idPelicula}, fecha_renta='{self.fecha_renta}', dias_de_renta={self.dias_de_renta}, estatus={self.estatus}, fecha_devolucion='{self.fecha_devolucion}')>"
