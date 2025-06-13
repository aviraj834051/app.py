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
    token = None
    if request.method == 'POST':
        cookie = request.form.get('cookie')
        token = extract_token(cookie)
    return f"""
    <h2 style='color:white;'>🛠️ Facebook EAAD Token Extractor</h2>
    <form method='POST'>
        <textarea name='cookie' rows='6' cols='70' placeholder='Paste your FB cookies here' required></textarea><br><br>
        <button type='submit'>🔍 Extract Token</button>
    </form><br>
    {'<b style="color:lime;">Token:<br>' + token + '</b>' if token else ''}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
