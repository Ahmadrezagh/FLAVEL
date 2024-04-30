from flask import jsonify

def handle_errors(error):
    # Your error handling logic here
    response = jsonify({'error': str(error)})
    response.status_code = 500
    return response
