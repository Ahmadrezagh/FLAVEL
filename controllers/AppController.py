from flask import Blueprint, render_template
AppController_blueprint = Blueprint('AppController', __name__)

# Define your routes and controller logic here

def welcome():
    return render_template('welcome.html')