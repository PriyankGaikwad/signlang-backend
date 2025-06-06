from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Load config from instance/config.py
    app.config.from_pyfile('config.py', silent=True)

    # Register blueprints
    from .routes import sign_routes
    app.register_blueprint(sign_routes.bp)

    return app
