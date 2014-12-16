from flask import Blueprint


# Initialise Blueprint (Routing) for the file
postcode_view = Blueprint('postcodes_view', __name__)

# Boundaries
@postcode_view.route('/')
def get_postcodes():
    return 'Postcode'

# Rankings

# Data Sources
