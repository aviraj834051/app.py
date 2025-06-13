from flask import Flask, render_template, request
from token_extractor import get_token_from_cookies
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    token = None
    cookies_text = ""
    
    if request.method == 'POST':
        cookies_text = request.form.get('cookies', '')
        token = get_token_from_cookies(cookies_text)

    return render_template('token_form.html', token=token, request=request)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
