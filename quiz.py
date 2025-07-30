import json, random, webbrowser
from flask import Flask, render_template, jsonify

app = Flask(__name__)

with open('questions.json') as f:
    all_questions = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def get_questions():
    questions = random.sample(all_questions, min(40, len(all_questions)))
    return jsonify(questions)

if __name__ == '__main__': 
    webbrowser.open(f"http://127.0.0.1:{5005}")
    app.run(host='0.0.0.0', port=5005)