from flask import Flask, render_template, jsonify
import random
import json
import webbrowser
import threading

app = Flask(__name__)

# Load questions from JSON file
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

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000')

if __name__ == '__main__':
    threading.Timer(0, open_browser).start()
    app.run(debug=False)