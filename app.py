from flask import Flask, render_template, request, redirect, session, flash
from token_extractor import get_token_from_cookies

app = Flask(__name__)
app.secret_key = "avii_secret_key"
USERNAME = "aviirajj8340"
PASSWORD = "avirajraj"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            session["user"] = USERNAME
            return redirect("/dashboard")
        else:
            flash("Galat Username ya Password!", "error")
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/")
    
    token = None
    if request.method == "POST":
        cookies = request.form["cookies"]
        token = get_token_from_cookies(cookies)
    return render_template("home.html", token=token)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
