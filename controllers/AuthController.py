from flask import Blueprint, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from models.User import User
AuthController_blueprint = Blueprint('AuthController', __name__)
from database import db
from middleware.authenticate import auth
# Define your routes and controller logic here

def register():
    user = auth()
    if user:
        return redirect('/panel')
    
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('auth/register.html')


def login():
    user = auth()
    if user:
        return redirect('/panel')
    
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            # Login successful
            session['user_id'] = user.id  # Store user ID in session
            return redirect('/panel')
        else:
            # Invalid username or password
            return 'Invalid username or password'
    return render_template('auth/login.html')

def logout():
    session.pop('user_id', None)  # Remove user ID from session
    return redirect('/login')

