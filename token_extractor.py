import requests

def get_token_from_cookies(cookie):
    headers = {
        "Host": "business.facebook.com",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10)",
        "Accept": "*/*",
        "Cookie": cookie
    }

    try:
        response = requests.get("https://business.facebook.com/business_locations", headers=headers)
        if "EAAG" in response.text:
            token = response.text.split('["EAAG')[1].split('"')[0]
            return "EAAG" + token
        else:
            return None
    except Exception as e:
        print(f"Error while extracting token: {e}")
        return None
