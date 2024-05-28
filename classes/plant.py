#!/usr/bin/env python

# Import package
from flask_restful import Resource, Api, reqparse
import logging as lg
import json


# Api endpoint
class Plant(Resource):

    def __init__(self, plants) -> None:
        """self.name = "plant_name" # Name
        self.name_sc = "nom_scientifique" # Scientific name
        self.spring_wt = "spring_watering" # Spring number days watering (in days)
        self.summer_wt = "summer_watering" # Summer number days watering (in days)
        self.autumn_wt = "autumn_watering" # Autumn number days watering (in days)
        self.winter_wt = "winter_watering" # Winter number days watering (in days)"""
        self.plants = plants


    # 1 - Function to get plant
    def get(self, id):
        for plant in self.plants:
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
        for plant in self.plants:
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
        self.plants.append(plant)
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
        for plant in self.plants:
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
        self.plants.append(plant)
        lg.info("The plant {} has been created".format(id))
        return plant, 201
    
    # 4 - Function to delete plant
    def delete(self, id):
        global plants
        # Return a plant list without the plant with id in argument
        plants = [plant for plant in self.plants if plant["id"] != id]
        return "The plant {} has been deleted".format(id)