from sqlalchemy.orm import Session
from modelos.usuario import Usuario
from modelos.pelicula import Pelicula
from modelos.renta import Renta
import datetime

# Operaciones CRUD para Usuario
def agregar_usuario(session: Session, nombre, apPat, apMat, password, email, superUser, profilePicture=None):
    nuevo_usuario = Usuario(nombre=nombre, apPat=apPat, apMat=apMat, password=password, email=email, superUser=superUser, profilePicture=profilePicture)
    session.add(nuevo_usuario)
    session.commit()

def obtener_usuarios(session: Session):
    return session.query(Usuario).all()

def obtener_usuario_por_id(session: Session, id_usuario):
    return session.query(Usuario).get(id_usuario)

def actualizar_usuario(session: Session, id_usuario, **kwargs):
    usuario = obtener_usuario_por_id(session, id_usuario)
    if usuario:
        for key, value in kwargs.items():
            setattr(usuario, key, value)
        session.commit()

def eliminar_usuario(session: Session, id_usuario):
    usuario = obtener_usuario_por_id(session, id_usuario)
    if usuario:
        session.delete(usuario)
        session.commit()

# Operaciones CRUD para Pelicula
def agregar_pelicula(session: Session, nombre, genero, duracion, inventario):
    nueva_pelicula = Pelicula(nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)
    session.add(nueva_pelicula)
    session.commit()

def obtener_peliculas(session: Session):
    return session.query(Pelicula).all()

def obtener_pelicula_por_id(session: Session, id_pelicula):
    return session.query(Pelicula).get(id_pelicula)

def actualizar_pelicula(session: Session, id_pelicula, **kwargs):
    pelicula = obtener_pelicula_por_id(session, id_pelicula)
    if pelicula:
        for key, value in kwargs.items():
            setattr(pelicula, key, value)
        session.commit()

def eliminar_pelicula(session: Session, id_pelicula):
    pelicula = obtener_pelicula_por_id(session, id_pelicula)
    if pelicula:
        session.delete(pelicula)
        session.commit()

# Operaciones CRUD para Renta
def agregar_renta(session: Session, idUsuario, idPelicula, fecha_renta, dias_de_renta=5, estatus=False, fecha_devolucion=None):
    nueva_renta = Renta(idUsuario=idUsuario, idPelicula=idPelicula, fecha_renta=fecha_renta, dias_de_renta=dias_de_renta, estatus=estatus, fecha_devolucion=fecha_devolucion)
    session.add(nueva_renta)
    session.commit()

def obtener_rentas(session: Session):
    return session.query(Renta).all()

def obtener_renta_por_id(session: Session, id_renta):
    return session.query(Renta).get(id_renta)

def actualizar_renta(session: Session, id_renta, **kwargs):
    renta = obtener_renta_por_id(session, id_renta)
    if renta:
        for key, value in kwargs.items():
            setattr(renta, key, value)
        session.commit()

def eliminar_renta(session: Session, id_renta):
    renta = obtener_renta_por_id(session, id_renta)
    if renta:
        session.delete(renta)
        session.commit()

def eliminar_todos_los_registros(session):
    # Borrar todos los registros de cada tabla
    session.query(Renta).delete()
    session.query(Pelicula).delete()
    session.query(Usuario).delete()
    session.commit()
