#!/usr/bin/env python

# Import
from flask import Flask
from flask_restful import Resource, Api, reqparse
import logging as lg


app = Flask(__name__)
api = Api(app)

# data to test
plants = [
    { "id": 1, "name": "caoutchouc", "name_sc": "ficus elastica", "spring_wt": 7, "summer_wt": 7, "autumn_wt": 12, "winter_wt": 12 },
    { "id": 2, "name": "pilea", "name_sc": "pilea peperomioides", "spring_wt": 7, "summer_wt": 7, "autumn_wt": 9, "winter_wt": 12 },
    { "id": 3, "name": "fougere", "name_sc": "nephrolepis exalta blue bell", "spring_wt": 7, "summer_wt": 3, "autumn_wt": 7, "winter_wt": 9 },
    { "id": 4, "name": "faux philodendron", "name_sc": "monstera deliciosa", "spring_wt": 4, "summer_wt": 4, "autumn_wt": 7, "winter_wt": 10 },
    { "id": 5, "name": "test", "name_sc": "test_sc", "spring_wt": 4, "summer_wt": 4, "autumn_wt": 7, "winter_wt": 10 }
    ]


# Api endpoint
class Plant(Resource):

    # 1 - Function to get plant
    def get(self, id):
        for plant in plants:
            if(id == plant["id"]):
                return plant, 200
        return "Plant not in database", 404

    # 2 - Function to create new plant
    def post(self, id):
        parser = reqparse.RequestParser() # Flask parser to extract JSON data
        parser.add_argument("name")
        parser.add_argument("name_sc")
        parser.add_argument("spring_wt")
        parser.add_argument("summer_wt")
        parser.add_argument("autumn_wt")
        parser.add_argument("winter_wt")
        args = parser.parse_args() # extract

        # If plant already in db
        for plant in plants:
            if(id == plant["id"]): 
                return "The plant {} exist already in db".format(id), 400
        
        # If not in db create plant
        plant = {
            "id": id, 
            "name": args["name"], 
            "name_sc": args["name_sc"], 
            "spring_wt": args["spring_wt"], 
            "summer_wt": args["summer_wt"], 
            "autumn_wt": args["autumn_wt"], 
            "winter_wt": args["winter_wt"]
        }
        # Add the new plant to plants dictionary
        plants.append(plant)
        return plant, 201


    # 3 - Function to create or update plant
    def put(self, id):
        parser = reqparse.RequestParser() # Flask parser to extract JSON data
        parser.add_argument("name")
        parser.add_argument("name_sc")
        parser.add_argument("spring_wt")
        parser.add_argument("summer_wt")
        parser.add_argument("autumn_wt")
        parser.add_argument("winter_wt")
        args = parser.parse_args() # extract

        # If plant already in db, update existing plant
        for plant in plants:
            if(id == plant["id"]): 
                plant["name"] = args["name"],
                plant["name_sc"] = args["name_sc"],
                plant["spring_wt"] = args["spring_wt"],
                plant["summer_wt"] = args["summer_wt"],
                plant["autumn_wt"] = args["autumn_wt"],
                plant["winter_wt"] = args["winter_wt"]
                lg.info("The plant {} has been updated".format(id))
                return plant, 200
        
        # Else create plant
        plant = {
            "id": id, 
            "name": args["name"], 
            "name_sc": args["name_sc"], 
            "spring_wt": args["spring_wt"], 
            "summer_wt": args["summer_wt"], 
            "autumn_wt": args["autumn_wt"], 
            "winter_wt": args["winter_wt"]
        }
        # Add the new plant to plants dictionary
        plants.append(plant)
        lg.info("The plant {} has been created".format(id))
        return plant, 201
    
    # 4 - Function to delete plant
    def delete(self, id):
        global plants
        # Return a plant list without the plant with id in argument
        plants = [plant for plant in plants if plant["id"] != id]
        return "The plant {} has been deleted".format(id)
    

# URI format definition
api.add_resource(Plant, "/plant/<int:id>")
# "app.config["DEBUG"] = True" +  "app.run()"
app.run(debug=True, port = 5001) # default port 5000 not working