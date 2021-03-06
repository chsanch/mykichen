import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from bson.objectid import ObjectId

# app config

app = Flask(__name__)

# Mongo Config

app.config["MONGO_DBNAME"] = 'recipe_databases'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://localhost//')

mongo = PyMongo(app)


# display card on we website
@app.route('/')
@app.route('/display_card')
def display_card():
    return render_template("display_card.html",
                            recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            