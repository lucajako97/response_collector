import logging
from flask import Flask, request, jsonify, make_response

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

@app.route('/capabilities')
def handle_capabilities():
    # Log the incoming request
    log_request(request)

    response_data = {
        "entropy" : True,
        "key" : True,
        "algorithm" : "QKD",
        "localSystemID" : "Alice",
        "remoteSystemID" : [
         "Bob",
         "Eve"
     ]
    }

    status_code = 200

    response = make_response(jsonify(response_data), status_code)
    return response


@app.route('/entropy')
def handle_entropy():
    # log
    log_request(request)

    if request.method == 'GET':
        parameter_value = request.args.get('minentropy')
        print(f'minentropy received = {minentropy}')
        response_data = {
            "randomStr" : "rfu839t",
            "minentropy" : 128
        }

    status_code = 200

    response = make_response(jsonify(response_data), status_code)
    return response


@app.route('/key')
def handle_key():
    #log
    log_request(request)

    response_data = {
        "keyId" : "1726e9AE76234FB",
        "key" : "C90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA"
    }

    status_code = 200

    response = make_response(jsonify(response_data), status_code)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
