from flask import Flask, render_template, request, redirect
import requests, re

app = Flask(__name__)

# 🔐 Login Credentials
USERNAME = 'aviirajj8340'
PASSWORD = 'avirajraj'

# 🔓 Token Extractor Function
def extract_token(cookie_string):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; Pixel 5 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/412.0.0.27.112;]',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': cookie_string
    }
    try:
        res = requests.get('https://business.facebook.com/business_locations', headers=headers)
        token = re.search(r'EAAD[\w-]+', res.text)
        if token:
            return token.group(0)
        else:
            return "❌ Token nahi mila. Fresh aur sahi cookie daalo."
    except Exception as e:
        return f"🔥 Error: {str(e)}"

# 🧑‍💻 Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == USERNAME and request.form.get('password') == PASSWORD:
            return redirect('/tool')
    return render_template('login.html')

# ⚙️ Tool Page
@app.route('/tool', methods=['GET', 'POST'])
def tool():
    token = ''
    cookie = ''
    if request.method == 'POST':
        cookie = request.form.get('cookie')
        token = extract_token(cookie)
    return render_template('tool.html', token=token, cookie=cookie)

# 🟢 Run on Render
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
