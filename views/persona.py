from flask import Blueprint
from models.database import db_session
from models.persona import Persona


# Initialise Blueprint (Routing) for the file
persona_view = Blueprint('persona_view', __name__)

@persona_view.route('/')
def list_personas():
    return 'Personas List'


@persona_view.route('/<id>')
def get_persona():
    return 'Persona'

@persona_view.route('/', methods=["POST"])
def create_persona():
    p = Persona()
    db_session.add(p)
    db_session.commit()

    return 'POST Persona'

@persona_view.route('/<id>', methods=["PUT"])
def update_persona():
    p = Persona()
    db_session.add(p)
    db_dession.commit()

    return "Update persona"
