from flask import Flask
from api.restaurant import restaurant
from api.interface import interface
from api.routes import routes

def create_flask_app(config):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    app.register_blueprint(restaurant, url_prefix='/api/restaurant/')
    app.register_blueprint(interface, url_prefix='/api/interface/')
    app.register_blueprint(routes, url_prefix='/api/routes')
    return app


if __name__ == '__main__':
    app = create_flask_app("config.py")
    app.run()
