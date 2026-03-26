from flask import Flask, render_template
import sys
import logging
import requests
import os

app = Flask(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

# Use environment variables for microservice URLs, with default values
recipe_microservice_url = os.environ.get('RECIPE_MICROSERVICE_URL', 'http://localhost:50')
nutrition_microservice_url = os.environ.get('NUTRITION_MICROSERVICE_URL', 'http://localhost:90')

def get_microservice_data(endpoint):
    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle request errors (e.g., connection error, timeout)
        print(f"Error accessing microservice: {e}")
        return {"title": "Error accessing microservice"}

# The UI:
@app.route('/')
@app.route('/index.html')
def index():
    # Make calls to microservices
    recipe = get_microservice_data(recipe_microservice_url)
    nutrition = get_microservice_data(nutrition_microservice_url)
    
    # Render the template with the results
    return render_template('index.html',
                            recipe=recipe,
                            nutrition=nutrition)

@app.route('/health')
def health():
    return ""

if __name__ == '__main__':
    if len(sys.argv) < 2:
        logging.error(f"usage: {sys.argv[0]} port")
        sys.exit(-1)

    port = int(sys.argv[1])
    logging.info(f"start at port {port}")

    # Make it compatible with IPv6 if Linux
    if sys.platform == "linux":
        app.run(host='::', port=port, debug=True, threaded=True)
    else:
        app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
