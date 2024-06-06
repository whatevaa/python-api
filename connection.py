from sqlalchemy import create_engine
import logging as lg
import os
from dotenv import load_dotenv
load_dotenv('c:/Projects/python-api/.env') # Path to .env file where is store environment variables (ignore by gitignore file)
from models import Base
#import schemas as sc
from sqlalchemy import text

host="localhost"
user= os.environ.get('DB_USER')
password= os.environ.get('DB_PASS')
database= 'pyplant_test' # An existing db

db_url = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}" # Connect MySQL to sqlAlchemy in python with mysqlconnector
#db_url = "mysql+mysqlconnector://{user}:{password}@{host}/{database}".format(user=user, password=password, host=host, database=database) # Connect MySQL to sqlAlchemy in python with mysqlconnector

engine = create_engine(db_url, echo=True) # echo=True to see the commands SQLAlchemy is sending
Base.metadata.create_all(engine) # to create tables, with schemas in models.py
"""
try:
    #connection = engine.connect()
    #print(connection)
    #Base.metadata.create_all(bind=connection)
    
    with engine.connect() as connection:
        print(connection)
        Base.metadata.create_all(bind=connection) # metadata.create_all not working with connection var, with mysqlconnector
        result = connection.execute(text("select plant_name from plant")) # test connection: OK
        for row in result:
            print("plant_name:", row.plant_name)
except Exception as e:
    lg.info(e)"""