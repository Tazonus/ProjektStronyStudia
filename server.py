from flask import Flask, render_template
import matplotlib.pyplot as plt
from collections import Counter

app = Flask(__name__)

@app.route('/')
def index(word = ''):
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/project')
def project():
    return render_template('project.html')
@app.route('/math')
def math():
    return render_template('math.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')