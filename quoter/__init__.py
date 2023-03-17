import os

from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'quoter.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize Database
    from . import db
    db.init_app(app)

    # Register Blueprints
    from . import root
    app.register_blueprint(root.bp)
    from . import auth
    app.register_blueprint(auth.bp)

    return app
