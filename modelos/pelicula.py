from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Pelicula(Base):
    __tablename__ = 'peliculas'
    
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45))
    duracion = Column(Integer)
    inventario = Column(Integer, nullable=False, default=1)

    rentas = relationship("Renta", back_populates="pelicula")

    def __repr__(self):
        return f"<Pelicula(idPelicula={self.idPelicula}, nombre='{self.nombre}', genero='{self.genero}', duracion={self.duracion}, inventario={self.inventario})>"