from flask import Flask

def setup_blueprints(app):
    from views.persona import persona_view
    from views.ranks import ranks_view
    #app.register_blueprint(geodata_view, url_prefix='/geodata')
    app.register_blueprint(persona_view, url_prefix='/persona')
    app.register_blueprint(ranks_view, url_prefix='/ranks')


app = Flask(__name__)
setup_blueprints(app)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
