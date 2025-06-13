from flask import Flask, render_template, request, redirect
import requests, re

app = Flask(__name__)

USERNAME = 'aviirajj8340'
PASSWORD = 'avirajraj'

def extract_token(cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10)',
        'Accept': '*/*',
        'Cookie': cookie,
    }
    response = requests.get('https://business.facebook.com/business_locations', headers=headers)
    match = re.search(r'EAAD\w+', response.text)
    if match:
        return match.group(0)
    return None

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            return redirect('/tool')
    return render_template('login.html')

@app.route('/tool', methods=['GET', 'POST'])
def tool():
    token = None
    if request.method == 'POST':
        cookie = request.form['cookie']
        token = extract_token(cookie)
    return f'''
    <h2 style="color:white;">Token Extractor</h2>
    <form method="POST">
        <textarea name="cookie" rows="5" cols="50" placeholder="Paste FB Cookie" required></textarea><br><br>
        <button type="submit">🔓 Extract Token</button>
    </form>
    <br>
    {'<b style="color:lime;">Token: ' + token + '</b>' if token else ''}
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
