from flask import request, current_app

def log_request():
    current_app.logger.info('Request Headers: %s', request.headers)
    current_app.logger.info('Request Method: %s', request.method)
    current_app.logger.info('Request Path: %s', request.path)
    current_app.logger.info('Request Data: %s', request.data)