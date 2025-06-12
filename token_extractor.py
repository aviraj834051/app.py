import requests
import re

def get_token_from_cookies(cookie_str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10)',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': cookie_str
    }

    try:
        res = requests.get("https://business.facebook.com/business_locations", headers=headers)
        access_token = re.search(r'EAAG\w+', res.text)
        if access_token:
            return access_token.group(0)
        else:
            return "❌ Token nahi nikla. Cookie check karo!"
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
