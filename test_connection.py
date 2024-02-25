from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('mysql+pymysql://luis:Developer123!@localhost/lab_ing_software')

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT VERSION()"))
        version = result.fetchone()
        print(f"Conexión exitosa. Versión de MySQL: {version[0]}")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
