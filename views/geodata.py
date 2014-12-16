from flask import Blueprint


# Initialise Blueprint (Routing) for the file
geodata_view = Blueprint('geodata_view', __name__)

# Boundaries
@geodata_view.route('/')
def get_boundaries():
    return 'Boundaries'


# Rankings

# Data Sources
