from geoalchemy import Column, GeometryColumn, Polygon, GeometryDDL
from sqlalchemy import Text, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

import datetime

Base = declarative_base()

class Postcodes (Base):
   __tablename__ = 'postcodes'
   postcode = Column (String, index=True, primary_key=True)
   geometry = GeometryColumn(Polygon(2))

   def __init__ (self, postcode = None, geometry=None):
      self.postcode = postcode
      self.geometry = geometry

GeometryDDL(Postcodes.__table__)
