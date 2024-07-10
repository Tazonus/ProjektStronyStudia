from flask import Flask, render_template, request

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
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Tutaj można dodać kod do przetwarzania danych formularza, np. zapisywanie do bazy danych lub wysyłanie emaila
    print(f"Name: {name}, Email: {email}, Message: {message}")
    return 'Wiadomość została wysłana pomyślnie!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')