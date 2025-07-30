# Local running: Open http://127.0.0.1:5005/ in browser
# Use number keys to select alternative, hit space to submit answer

from flask import Flask, render_template, jsonify
import random
import json
import os

app = Flask(__name__)

with open('questions.json') as f:
    all_questions = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def get_questions():
    num_questions = min(40, len(all_questions))  # Avoid selecting more questions than available
    selected_questions = random.sample(all_questions, num_questions)
    return jsonify(selected_questions)

if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT', 5005))
    except ValueError:
        port = 5005

    app.run(host='0.0.0.0', port=port, debug=False)