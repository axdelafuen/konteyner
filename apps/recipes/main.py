from flask import Flask, jsonify
import requests
import random
import sys
import logging
import os

app = Flask(__name__)

# Use the 'INGREDIENTS_API_URL' environment variable if available; otherwise, use the default URL
ingredients_api_url = os.environ.get('INGREDIENTS_API_URL', 'http://localhost:80')

def get_ingredients_data():
    response = requests.get(ingredients_api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def generate_recipe(ingredients_data, num_ingredients=3):
    # Shuffle the list of ingredients
    random.shuffle(ingredients_data)
    
    # Take a random subset of ingredients
    selected_ingredients = random.sample(ingredients_data, min(num_ingredients, len(ingredients_data)))
    
    # Calculate the sum of calories
    total_calories = sum(ingredient['calories'] for ingredient in selected_ingredients)
    
    # Replace this with your recipe generation logic
    # Here, we create a dictionary with 'name' and 'calories' keys
    recipe = {
        'name': " ".join([ingredient['ingredient'] for ingredient in selected_ingredients]),
        'calories': total_calories
    }
    
    return recipe

@app.route('/', methods=['GET'])
def get_random_recipe():
    ingredients_data = get_ingredients_data()
    
    if ingredients_data:
        recipe = generate_recipe(ingredients_data)
        return jsonify(recipe)
    else:
        return jsonify({'error': 'Failed to fetch ingredients data'})

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
