from flask import Flask, render_template
from database import db
from dotenv import load_dotenv
import os
from middleware.logging import log_request
from middleware.error_handling import handle_errors

from controllers import PanelController
from controllers import AuthController
from controllers import AppController

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
# Register middleware functions
app.before_request(log_request)
app.register_error_handler(500, handle_errors)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize SQLAlchemy with the Flask app
db.init_app(app)
with app.app_context():
    db.create_all()

app.route("/")(AppController.welcome)
app.route('/panel')(PanelController.index)
app.route('/login',methods=['POST','GET'])(AuthController.login)
app.route('/register',methods=['POST','GET'])(AuthController.register)
app.route('/logout',methods=['POST','GET'])(AuthController.logout)

