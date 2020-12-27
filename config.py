import os
from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['MONGO_DBNAME'] = "PERSON_EXPENSE_INVENTORY"
app.config['MONGO_URI'] = "mongodb://localhost:27017/PERSON_EXPENSE_INVENTORY"
mongo = PyMongo(app)
