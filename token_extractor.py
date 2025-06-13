import requests
import re

def extract_token_from_cookie(cookie_str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": cookie_str,
    }

    session = requests.Session()
    try:
        response = session.get("https://business.facebook.com/business_locations", headers=headers)
        token = re.search(r'EAAG\w+', response.text)
        if token:
            return token.group(0)
        else:
            return None
    except Exception as e:
        return None
