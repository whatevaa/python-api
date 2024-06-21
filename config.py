# Import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from dotenv import load_dotenv
load_dotenv('c:/Projects/python-api/.env') # Path to .env file where is store environment variables (ignore by gitignore file)

# Connexion information
host="localhost"
user= os.environ.get('DB_USER')
password= os.environ.get('DB_PASS')
database= 'pyplant_test' # An existing db
db_url = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}" # Connect MySQL to sqlAlchemy in python with mysqlconnector

# Class to help config
class Config:
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Removes obnoxious track mods warning
    FLASK_DEBUG = True

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy and Marshmallow with app context
db = SQLAlchemy(app) # instantiate DB within app
ma = Marshmallow(app)

# Add db to app configuration.
# as we can not use __init__ constructor in API classes (example PlantApi), 
# as app.py/api.add_resource only accept a class and not a class instance
app.config['db'] = db