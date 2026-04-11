from flask import Flask, jsonify
import random

app = Flask(__name__)

# Sample data (can be replaced with database later)
recipes = ["Fried Rice", "Pancake", "Spaghetti", "Salad"]

@app.route('/')
def home():
    return "Omakase Home"

@app.route('/random')
def random_recipe():
    recipe = random.choice(recipes)
    return jsonify({"recipe": recipe})

if __name__ == '__main__':
    app.run(debug=True)