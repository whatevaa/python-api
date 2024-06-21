#!/usr/bin/env python

# Import package
from flask_restful import Resource
from flask import request, current_app
from models import Plant, User, UserPlantEvent
from schemas import plant_schema, plants_schema


# Api endpoint
class PlantApi(Resource):

    # 1 - Function to get plant
    def get(self, id=None):
        if not id:
            plants = Plant.query.all()
            return plants_schema.dump(plants), 200
        else:
            plant = Plant.query.get(id)
            if not plant:
                return "Plant not in database", 404
            return plant_schema.dump(plant), 200

    # 2 - Function to create new plant
    def post(self):
            sname = request.json['scientific_name']
            existing_plant = Plant.query.filter(Plant.scientific_name == sname).one_or_none()
            if existing_plant is None:
                new_plant = plant_schema.load(request.json, session=current_app.config['db'].session)
                current_app.config['db'].session.add(new_plant)
                current_app.config['db'].session.commit()
                return plant_schema.dump(new_plant), 201
            else:
                return "The plant {} exist already in db with id {}".format(sname,existing_plant.id), 400

    # 3 - Function to create or update plant
    def put(self, id):
        existing_plant = Plant.query.get(id)
        if existing_plant is None:
            return {"message": "Plant not found"}, 404
        updated_plant = plant_schema.load(request.json, instance=existing_plant, session=current_app.config['db'].session) # to update the plant use instance=existing_plant, if not a new plant is created
        current_app.config['db'].session.add(updated_plant)
        current_app.config['db'].session.commit()
        return plant_schema.dump(updated_plant), 201

    # 4 - Function to delete plant
    def delete(self, id):
        plant_to_delete = Plant.query.get(id)
        if plant_to_delete is None:
            return {"message": "Plant not found"}, 404
        current_app.config['db'].session.delete(plant_to_delete)
        current_app.config['db'].session.commit()
        return {"message": "Plant has been deleted"}, 204