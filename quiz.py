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

    print(f"\nQuiz app running! Open http://127.0.0.1:{port} in your browser.")
    print("Use number keys (1–4) to select an answer, and spacebar to go to the next question.\n")

    app.run(host='0.0.0.0', port=port, debug=False)