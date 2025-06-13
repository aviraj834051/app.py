from flask import Flask, render_template, request, redirect
import requests, re

app = Flask(__name__)

USERNAME = 'aviirajj8340'
PASSWORD = 'avirajraj'

def extract_token(cookie_string):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12)',
        'Accept': '*/*',
        'Cookie': cookie_string
    }
    try:
        r = requests.get('https://business.facebook.com/business_locations', headers=headers)
        token = re.search(r'EAAD\w+', r.text)
        return token.group(0) if token else None
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == USERNAME and request.form.get('password') == PASSWORD:
            return redirect('/tool')
    return render_template('login.html')

@app.route('/tool', methods=['GET', 'POST'])
def tool():
    token = ''
    cookie = ''
    if request.method == 'POST':
        cookie = request.form.get('cookie')
        token = extract_token(cookie)
    return render_template('tool.html', token=token, cookie=cookie)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
