# python-api

This project consists of making a REST api in python with a set of plant data (in a mysql database).
The aim is to be able to call this data with methods: Get, Post, Put, Delete.

## Project archi :

```
python-api/
│
├── app.py
├── models.py
├── schemas.py
├── config.py
└── classes/
    └── plant.py
    └── user.py
    └── userplantevent.py
```

## Description 
- `config.py`: Contains the database information connection, the Config class and initializes the Flask, SQLAlchemy and Marshmallow application (to avoid circular import).
- `app.py` : The main application file which imports configurations from config.py, initializes the Flask-RESTful API and registers resources.
- `models.py` : Contains the definitions of the SQLAlchemy models using the db instance imported from config.py.
- `schemas.py` : Contains the Marshmallow schema definitions using the ma instance imported from config.py.
- `classes/plant.py` : Contains the PlantApi class for managing REST API requests related to plants.
- `classes/user.py` : Contains the UserApi class for managing REST API requests related to users.
- `classes/userplantevent.py` : Contains the UserPlantEventApi class for managing REST API requests related to events.

## The data:
- **plants**
    - *id*: unique id of the plant
    - *name*: its name in everyday language
    - *scientific_name*: its scientific name
    - *spring_wt*: Every time the plant needs to be watered in spring (in days)
    - *summer_wt*: Every time the plant needs to be watered in summer (in days)
    - *autumn_wt*: Every time the plant needs to be watered in autumn (in days)
    - *winter_wt*: Every time the plant needs to be watered in winter (in days)

## Packages

- **Flask** is a Python web application frameworks that can help to create an API
    - [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- **Marshmallow** is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.
    - Convert data from one data structure to another. 
    - [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
- **Flask-marshmallow** is a Flask (a Python web framework) extension for Marshmallow (an object serialization/deserialization library) that makes it easier to use Marshmallow with Flask. This integration layer for Flask and marshmallow also allow to generate URLs and hyperlinks for Marshmallow objects.
    - Serialization/deserialization and creating DTOs (data transfer objects)
    - [Flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- **Marshmallow-sqlalchemy** is an extension of Marshmallow for SQLAlchemy (an SQL Object Relational Mapper).
    - [Marshmallow-sqlalchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)
- **Flask-SQLAlchemy** is an extension for Flask that adds support for SQLAlchemy to your application. 
    - [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)


## Notes
- Flask-RESTful crée l'instance de la classe sans arguments. 
    - Donc on passe directement la classe *PlantApi* à `api.add_resource` (et non une instance de classe:  ~~*PlantApi(db)*~~). 
    - Ainsi on ne peut pas utiliser un constructeur (`__init__`) dans la classe *PlantApi* pour passer la session de la base de données `self.db = db `(ou toute autre dépendance) à l'instance de la classe. 
    - Nous pouvons par contre accéder à la base de données via le contexte d'application Flask, en utilisant `current_app.config['db']`
