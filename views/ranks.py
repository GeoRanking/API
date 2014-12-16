from flask import Blueprint
from core.ranking import Ranking


# Initialise Blueprint (Routing) for the file
ranks_view = Blueprint('ranks_view', __name__)

# Boundaries
@ranks_view.route('/')
def get_ranks():
    return 'Ranks'
