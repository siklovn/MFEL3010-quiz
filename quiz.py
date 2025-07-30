import json
import random
import webbrowser
from flask import Flask, render_template, jsonify

JSON_FILE       = 'questions.json'
NUM_QUESTIONS   = 40                # Set number of questions in test
PORT            = 5005              # Adjust port if needed

app = Flask(__name__)

with open(JSON_FILE) as f:
    all_questions = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def get_questions():
    num_questions = min(NUM_QUESTIONS, len(all_questions))
    selected_questions = random.sample(all_questions, num_questions)
    return jsonify(selected_questions)

if __name__ == '__main__':     # Adjust if needed
    url = f"http://127.0.0.1:{PORT}"
    print(f"\nLaunching quiz app at {url}\n")
    webbrowser.open(url)
    app.run(host='0.0.0.0', port=PORT, debug=False)