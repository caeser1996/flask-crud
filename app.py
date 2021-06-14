#Flask
from flask import Flask
#Pymongo
from flask_pymongo import PyMongo

app = Flask(__name__, static_url_path='')
app.secret_key = "test app"
app.config["MONGO_URI"]="mongodb://localhost:27017/trainingsession"

mongo = PyMongo(app)




# it will hold all the base libraries and configs

