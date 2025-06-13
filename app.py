from flask import Flask, render_template, request, redirect, session
from token_extractor import extract_token
import os

app = Flask(__name__)
app.secret_key = "avii_secure_key"

USERNAME = "aviirajj8340"
PASSWORD = "avirajraj"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        passwd = request.form['password']
        if uname == USERNAME and passwd == PASSWORD:
            session['logged_in'] = True
            return redirect('/token')
        else:
            return "Incorrect credentials", 403
    return render_template("login.html")

@app.route('/token', methods=['GET', 'POST'])
def token_page():
    if not session.get('logged_in'):
        return redirect('/')
    if request.method == 'POST':
        cookie = request.form['cookie']
        try:
            token = extract_token(cookie)
            return f"<h3 style='color:lime;'>✅ Extracted Token:</h3><textarea rows=6 cols=90>{token}</textarea>"
        except Exception as e:
            return f"<h3 style='color:red;'>❌ Error:</h3> {str(e)}"
    return render_template("token_form.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
