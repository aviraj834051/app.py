from flask import Flask, render_template, request
from token_extractor import get_token_from_cookies

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    eaab_token = ""
    eaad_token = ""
    if request.method == "POST":
        cookies = request.form["cookies"]
        token = get_token_from_cookies(cookies)

        if token.startswith("EAAD"):
            eaad_token = token
        elif token.startswith("EAAB"):
            eaab_token = token

    return render_template("home.html", eaad_token=eaad_token, eaab_token=eaab_token)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
