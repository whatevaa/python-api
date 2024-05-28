#!/usr/bin/env python

# Import
from flask import Flask
from flask_restful import Resource, Api, reqparse
import logging as lg
import json
import sys 
import os
# Add to sys.path the repository PyPlant/classes, if not already in
if os.path.abspath("classes") not in sys.path :
    sys.path.append(os.path.abspath("classes"))
import plant # import python-api/classes/plant.py


app = Flask(__name__)
api = Api(app)

# data to test
plants_data = [] # list with json objects (dicts)
with open('plants_data.json') as json_file:
   plants_data = json.load(json_file)

# Plant object
plant_object = plant.Plant # from class Plant() in python-api/classes/plant.py

# URI format definition
# "resource_class_kwargs" to pass data as parameter into a Flask-RESTfull Resource.
# Because we want to pass plants_data to the class Plant(), to use functions 
api.add_resource(plant_object, "/plant/<int:id>", resource_class_kwargs={'plants': plants_data}) 
# "app.config["DEBUG"] = True" +  "app.run()"
app.run(debug=True, port = 5001) # default port 5000 not working