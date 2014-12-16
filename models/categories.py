from middleware import app
import datetime

class Categories (db):
   __tablename__ = 'categories'
   id = Column (Integer, index=True, primary_key=True)
   persona_id = Column (Integer, unique=False)
   postcode = Column (String, unique=False)
   category_name = Column (String, unique=False)
   category_weight = Column (Integer, unique=False)
   category_rank = Coumn (Integer, unique=False)

   def __init__ (self, persona_id = None, postcode = None, category_name = None,
                    category_weight = None, category_rank = None):
      self.persona_id = persona_id
      self.name = name
      self.postcode = postcode
      self.category_name = category_name
      self.category_weight = category_weight
      self.category_rank = category_rank
