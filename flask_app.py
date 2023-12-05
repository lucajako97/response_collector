import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='requests.log', level=logging.INFO)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    # Log the incoming request
    log_request(request)

    # Respond with a JSON object
    response_data = {
        "message": "Hello, this is a static response!",
        "status": "success"
    }
    return jsonify(response_data)

def log_request(request):# Log request method, URL, and headers to console
    app.logger.info(f"Request Method: {request.method}")
    app.logger.info(f"Request URL: {request.url}")
    app.logger.info(f"Request Headers: {request.headers}")

    # Log request data for POST requests to console
    if request.method == 'POST':
        app.logger.info(f"Request Data: {request.data}")

    # Log request details to file
    logging.info(f"Request Method: {request.method}")
    logging.info(f"Request URL: {request.url}")
    logging.info(f"Request Headers: {request.headers}")

    # Log request data for POST requests to file
    if request.method == 'POST':
        logging.info(f"Request Data: {request.data}")

if __name__ == '__main__':
    app.run(debug=True)
