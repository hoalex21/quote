from flask import Flask

from flask_sqlalchemy import SQLAlchemy


# Create and configure the app
app = Flask(__name__)
app.config ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quote.db"

# Database
db = SQLAlchemy(app)

def create_app():
    # Register Blueprints
    from . import root
    app.register_blueprint(root.bp)
    from . import auth
    app.register_blueprint(auth.bp)

    return app
