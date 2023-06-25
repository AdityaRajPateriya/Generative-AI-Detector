from flask import Flask, render_template, request
from model import GPT2PPL

# Initialize the Flask app
app = Flask(__name__)

# Initialize the model
model = GPT2PPL()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sentence = request.form['sentence']
        results, output = model(sentence)
        return render_template('result.html', sentence=sentence, results=results, output=output)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
