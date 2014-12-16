from middleware import app
import datetime

class Ranks (db):
   __tablename__ = 'ranks'
   id = Column (Integer, index=True, primary_key=True)
   persona_id = Column (Integer, unique=False)
   postcode = Column (String, unique=False)
   rank = Column (Integer, index=True, primary_key=False)

   def __init__ (self, persona_id = None, postcode = None, rank = None):
      self.persona_id = persona_id
      self.postcode = postcode
      self.rank = rank
