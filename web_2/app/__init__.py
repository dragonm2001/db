import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

alch = SQLAlchemy()
bc = Bcrypt()

load_dotenv()

def create_app(config_name='DevConfig'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    app.config['ENCRYPTION_KEY'] = os.getenv('ENCRYPTION_KEY')
    alch.init_app(app)
    bc.init_app(app)
    app.bcrypt = bc

    from .routers import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app