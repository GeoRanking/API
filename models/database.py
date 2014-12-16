import sqlite3
from sqlalchemy import event, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy import Geometry, GeometryColumn, GeometryDDL, WKTSpatialElement
from flask import g

DATABASE_URI = "sqlite:////var/www/database/database.sqlite"

engine = create_engine(DATABASE_URI, convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

@event.listens_for(engine, "connect")
def connect(conn, conn_rec):
    conn.enable_load_extension(True)
    conn.execute("select load_extension('/usr/local/lib/mod_spatialite.so')")
    conn.enable_load_extension(False)

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    #from geodata import geodata
    import persona
    from data.postcodes import Postcodes
    Base.metadata.create_all(bind=engine)
