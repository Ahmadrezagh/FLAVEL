from flask import request, session

from models.User import User

def auth():
    user_id = session.get('user_id')
    if user_id:
        return User.query.get(user_id)
    return None
    
