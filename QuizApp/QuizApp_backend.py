# QuizApp_backend.py

from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Sample celebrity names
celebrities = [
    'Brad Pitt', 'Angelina Jolie', 'Tom Hanks', 'Jennifer Aniston', 'Leonardo DiCaprio',
    'Emma Watson', 'Chris Hemsworth', 'Scarlett Johansson', 'Will Smith', 'Meryl Streep'
]

# Shuffle the celebrities to create a random order
random.shuffle(celebrities)

@app.route('/')
def home():
    # Display the first celebrity in the shuffled list
    current_celebrity = celebrities[0]
    return render_template('index.html', current_celebrity=current_celebrity)

@app.route('/submit', methods=['POST'])
def submit():
    user_guess = request.form.get('user_guess')
    current_celebrity = celebrities[0]

    return render_template('result.html', user_guess=user_guess, correct_celebrity=current_celebrity)

if __name__ == '__main__':
    app.run(debug=True)
