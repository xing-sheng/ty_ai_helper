from flask import Flask, render_template, request, jsonify
from src.core.ai_service import ask_ai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    answer = ask_ai(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
