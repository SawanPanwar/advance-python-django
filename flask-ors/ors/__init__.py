from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, template_folder="template")

    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    # Models register
    from .models import User, Role

    # Routes register
    from .routes import main_bp

    app.register_blueprint(main_bp)

    return app
