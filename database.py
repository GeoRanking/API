import geoalchemy

print 'Creating database'
from models.database import init_db
init_db()
print 'Database created'
