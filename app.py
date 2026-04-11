from flask import Flask
import random

app = Flask(__name__)

recipes = ["Nasi Lemak", "Fried Rice", "Pasta", "Burger"]

@app.route('/')
def home():
    recipe = random.choice(recipes)
    return f"<h1>Omakase Today</h1><p>You should eat: {recipe}</p>"

if __name__ == '__main__':
    app.run(debug=True)