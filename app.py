#!/usr/bin/env python

# Import
from flask_restful import Api
import sys 
import os
# Add to sys.path the repository python-api/classes, if not already in
if os.path.abspath("classes") not in sys.path :
    sys.path.append(os.path.abspath("classes"))
from classes.plant import PlantApi # import python-api/classes/plant.py
from classes.user import UserApi 
from config import app, db

# Plant object (from class PlantApi in python-api/classes/plant.py)
plant_object = PlantApi # Do not use a class instance (ex: plant_object = PlantApi(db)) and remove constructor in PlantApi
user_object = UserApi

# URI format definition
api = Api(app)
api.add_resource(plant_object, "/plant", "/plant/<int:id>")
api.add_resource(user_object, "/user", "/user/<int:id>")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True, port = 5001) # default port 5000 not working