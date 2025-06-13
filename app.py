from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("token_form.html")

@app.route('/get_token', methods=['POST'])
def get_token():
    cookie = request.form.get('cookie')

    # Dummy logic: Check if cookie is valid format
    if "c_user=" in cookie and "xs=" in cookie:
        # In real project, yahan Facebook token extraction logic lagana hai
        token = "EAABwzLixnjYBA-FakeTokenExample..."  # Replace with real logic
        return f"""
        <h2 style='color:lime;'>✅ Token mil gaya!</h2>
        <textarea rows='4' cols='50'>{token}</textarea><br><br>
        <a href='/'>🔙 Wapas jao</a>
        """
    else:
        return """
        <h2 style='color:red;'>❌ Invalid Cookie Format</h2>
        <a href='/'>🔙 Try Again</a>
        """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
