from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from modules.equipos import bp as bpequipos
    from modules.evaluaciones import bp as bpdatos

    app.register_blueprint(bpequipos)
    app.register_blueprint(bpdatos)

    return app
