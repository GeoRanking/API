from geoalchemy import Column
from sqlalchemy import Text, Integer, String, DateTime

import datetime

class Persona ():
   __tablename__ = 'persona'
   id = Column (Integer, index=True, primary_key=True)
   original_id = Column (Integer, unique=False)
   name = Column (String, unique=False)
   details = Column (Text, unique=False)
   date_time = Column (DateTime, unique=False)

   def __init__ (self, original_id = None, name = None, details = None):
      self.original_id = original_id
      self.name = name
      self.details = details
      self.date_time = datetime.datetime.now()
