from flask import Blueprint


# Initialise Blueprint (Routing) for the file
categories_view = Blueprint('categories_view', __name__)

# Boundaries
@categories_view.route('/')
def get_categories():
    return 'Categories'

# Rankings

# Data Sources
