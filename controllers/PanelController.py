from flask import Blueprint, render_template
PanelController_blueprint = Blueprint('PanelController', __name__)

from middleware.authenticate import auth

# Define your routes and controller logic here

def index():
    user = auth()
    if user:
        return render_template("panel.html")