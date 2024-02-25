from sqlalchemy import Column, Integer, String, LargeBinary, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    apPat = Column(String(200), nullable=False)
    apMat = Column(String(200))
    password = Column(String(64), nullable=False)
    email = Column(String(500), unique=True)
    profilePicture = Column(LargeBinary)
    superUser = Column(Boolean)

    rentas = relationship("Renta", back_populates="usuario")

    def __repr__(self):
        return f"<Usuario(idUsuario={self.idUsuario}, nombre='{self.nombre}', apPat='{self.apPat}', apMat='{self.apMat}', email='{self.email}')>"
