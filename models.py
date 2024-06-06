from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

print('creating Base')
Base = declarative_base()

class Plant(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True, index=True) # SQLAlchemy will automatically set the first Integer PK column that's not marked as a FK as autoincrement=True.
    name = Column(String(40), unique=True, index=True)
    scientific_name = Column(String(40), unique=True, index=True)
    spring_wt = Column(Integer, index=True)
    summer_wt = Column(Integer, index=True)
    autumn_wt = Column(Integer, index=True)
    winter_wt = Column(Integer, index=True)

    user_plant_event = relationship("UserPlantEvent", back_populates="plant")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), index=True)
    last_name = Column(String(40), index=True)
    pseudo = Column(String(40), unique=True, index=True)
    mail = Column(String(40), unique=True, index=True)

    user_plant_event = relationship("UserPlantEvent", back_populates="user")


class UserPlantEvent(Base):
    __tablename__ = 'user_plant_event'

    id = Column(Integer, primary_key=True, index=True)
    date_last_wt = Column(Date, index=True)
    date_next_wt = Column(Date, index=True)

    plant_id = Column(Integer, ForeignKey("plants.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    plant = relationship("Plant", back_populates="user_plant_event")
    user = relationship("User", back_populates="user_plant_event")