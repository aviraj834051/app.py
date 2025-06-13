from flask import Flask, render_template, request, redirect, session
from token_extractor import extract_token_from_cookie

app = Flask(__name__)
app.secret_key = 'secret_key_aviiraj'  # Secret key for session

USERNAME = "aviirajj8340"
PASSWORD = "avirajraj"

@app.route('/')
def login():
    return render_template("login.html")

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
def cookie():
    if 'user' in session:
        return render_template("cookie_input.html")
    else:
        return redirect('/')

@app.route('/home', methods=['POST'])
def home():
    if 'user' not in session:
        return redirect('/')
    cookie = request.form['cookie']
    token = extract_token_from_cookie(cookie)
    return render_template("home.html", token=token)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
