import requests
import re

def extract_token(cookies_string):
    cookies = {}
    for item in cookies_string.split(";"):
        key, value = item.strip().split("=", 1)
        cookies[key] = value

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10)",
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get("https://business.facebook.com/business_locations", headers=headers, cookies=cookies)
    access_token = re.search(r'EAAG\w+', response.text)

    if access_token:
        return access_token.group(0)
    else:
        raise Exception("Valid group-messaging token not found. Check your Facebook account settings.")
