from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate


# Create and configure the app
app = Flask(__name__)
app.config ["SECRET_KEY"] = "dev"
app.config ["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///quote.db'

# Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask Login
login_manager = LoginManager(app)

# Bcrypt
bcrypt = Bcrypt(app)

# Register Blueprints
from quoter.root.routes import root
app.register_blueprint(root)
from quoter.users.routes import users
app.register_blueprint(users)

def create_app():
    return app
