# Import
from config import ma
from models import Plant, User, UserPlantEvent

class PlantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Plant
        load_instance = True
        fields = ("id", "name", "scientific_name", "spring_wt", "summer_wt", "autumn_wt", "winter_wt") # List of fields to be included in serialisation, explicitly specifying their order.
        ordered = True  # Ensures that fields are returned in the order specified in fields.
    #user_plant_events = ma.Nested("UserPlantEventSchema", many=True)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        fields = ("id", "name", "last_name", "pseudo", "mail") # List of fields to be included in serialisation, explicitly specifying their order.
        ordered = True  # Ensures that fields are returned in the order specified in fields.
    #user_plant_events = ma.Nested("UserPlantEventSchema", many=True)

class UserPlantEventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserPlantEvent
        load_instance = True
        fields = ("id", "date_last_wt", "date_next_wt", "plant_id", "user_id") # List of fields to be included in serialisation, explicitly specifying their order.
        ordered = True  # Ensures that fields are returned in the order specified in fields.
    #user = ma.Nested(UserSchema)
    #plant = ma.Nested(PlantSchema)

plant_schema = PlantSchema()
plants_schema = PlantSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)
user_plant_event_schema = UserPlantEventSchema()
user_plant_events_schema = UserPlantEventSchema(many=True)