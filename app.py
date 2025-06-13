from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def get_token_from_cookie(cookie_str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile)",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": cookie_str
    }

    response = requests.get("https://business.facebook.com/business_locations", headers=headers)
    try:
        token = response.text.split('EAAG')[1].split('"')[0]
        return "EAAG" + token
    except Exception as e:
        print("Error extracting token:", e)
        return None

@app.route('/')
def home():
    return render_template("token_form.html")

@app.route('/get_token', methods=['POST'])
def get_token():
    cookie = request.form.get('cookie')
    token = get_token_from_cookie(cookie)

    if token:
        return f"""
        <h2 style='color:lime;'>✅ Real Token mil gaya!</h2>
        <textarea rows='4' cols='50'>{token}</textarea><br><br>
        <a href='/'>🔙 Wapas jao</a>
        """
    else:
        return """
        <h2 style='color:red;'>❌ Token nahi nikla. Cookie galat ho sakti hai ya FB block kar raha ho.</h2>
        <a href='/'>🔙 Try Again</a>
        """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
