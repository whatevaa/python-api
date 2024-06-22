# Import package
from config import db

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True, index=True) # SQLAlchemy will automatically set the first Integer PK column that's not marked as a FK as autoincrement=True.
    name = db.Column(db.String(40), unique=True, index=True)
    scientific_name = db.Column(db.String(40), unique=True, index=True)
    spring_wt = db.Column(db.Integer, index=True)
    summer_wt = db.Column(db.Integer, index=True)
    autumn_wt = db.Column(db.Integer, index=True)
    winter_wt = db.Column(db.Integer, index=True)

    #user_plant_event = db.relationship("UserPlantEvent", back_populates="plant")
    def __repr__(self):
        return f'<Plant {self.name}>'


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(40), index=True)
    last_name = db.Column(db.String(40), index=True)
    pseudo = db.Column(db.String(40), unique=True, index=True)
    mail = db.Column(db.String(40), unique=True, index=True)

    #user_plant_event = db.relationship("UserPlantEvent", back_populates="user")
    def __repr__(self):
        return f'<User {self.name}>'


class UserPlantEvent(db.Model):
    __tablename__ = 'user_plant_event'

    id = db.Column(db.Integer, primary_key=True, index=True)
    date_last_wt = db.Column(db.Date, index=True)
    date_next_wt = db.Column(db.Date, index=True)

    plant_id = db.Column(db.Integer, db.ForeignKey("plants.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    #plant = db.relationship("Plant", back_populates="user_plant_event")
    #user = db.relationship("User", back_populates="user_plant_event")
    def __repr__(self):
        return f'<UserPlantEvent {self.id} for user {self.user_id} and plant {self.plant_id}>'