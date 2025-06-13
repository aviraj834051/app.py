from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    token = None
    if request.method == 'POST':
        cookies = request.form['cookies']
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "en-US,en;q=0.9"
        }
        try:
            session = requests.Session()
            cookie_dict = dict(item.split("=", 1) for item in cookies.split("; ") if "=" in item)
            session.cookies.update(cookie_dict)
            res = session.get("https://business.facebook.com/business_locations", headers=headers)
            eaad = res.text.split('EAAD')[1].split('"')[0]
            token = "EAAD" + eaad
        except:
            token = "❌ Invalid or expired cookie. Please try fresh one."

    return f'''
        <form method="POST">
            <textarea name="cookies" placeholder="Paste Facebook Cookies Here" rows="5" cols="80"></textarea><br>
            <button type="submit">Extract EAAD Token</button>
        </form>
        <br>
        <strong>Token:</strong> {token if token else ""}
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
