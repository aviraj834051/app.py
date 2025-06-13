from flask import Flask, render_template, request, redirect, session
from token_extractor import extract_token

app = Flask(__name__)
app.secret_key = "secret_key_aviiraj"

USERNAME = "aviirajj8340"
PASSWORD = "avirajraj"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username == USERNAME and password == PASSWORD:
        session['user'] = username
        return redirect('/cookie')
    else:
        return "Incorrect username or password!"

@app.route('/cookie')
def cookie_page():
    if 'user' not in session:
        return redirect('/')
    return render_template('home.html')

@app.route('/generate_token', methods=['POST'])
def generate_token():
    if 'user' not in session:
        return redirect('/')
    cookies = request.form['cookies']
    token = extract_token(cookies)
    return render_template('home.html', token=token)

if __name__ == '__main__':
    app.run(port=5000)
