from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
from collections import Counter

app = Flask(__name__)

@app.route('/')
def index():
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

@app.route('/send-message', methods=['POST'])
def send_message():
    message = request.form['message']
    print(f"Message: {message}")
    generate_letter_histogram(message)
    return send_file("plot.png")

def generate_letter_histogram(word):
    try:
        word = word.lower().replace(" ", "")
        letter_counts = Counter(word)
        letters = list(letter_counts.keys())
        counts = list(letter_counts.values())

        plt.bar(letters, counts, color='#218c74')
        plt.title('częstotliwość liter w podanym zdaniu')
        plt.xlabel('Litery')
        plt.ylabel('Liczba wystąpień')
        plt.savefig('plot.png')
        plt.close()
    except:
        index()
    #matplot gui is problematic in servers
    #this try except is saving it from crashing(mostly)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')