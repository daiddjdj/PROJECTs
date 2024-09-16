from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)


# creating routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    if request.method == 'POST':
        symptoms = request.form.get('symptoms')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/developer')
def developer():
    return render_template('developer.html')

# python main
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6173, debug=True)
