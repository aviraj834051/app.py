import re
import requests

def extract_token(cookies):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10)",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        jar = requests.cookies.RequestsCookieJar()
        cookie_parts = cookies.split(';')
        for part in cookie_parts:
            key, value = part.strip().split('=', 1)
            jar.set(key, value, domain=".facebook.com")

        response = requests.get("https://business.facebook.com/business_locations", headers=headers, cookies=jar)
        match = re.search(r'EAAG\w+', response.text)
        if match:
            return match.group(0)
        else:
            return "❌ Failed to extract Token. Use latest cookies from m.facebook.com or Android App."
    except Exception as e:
        return f"Error: {str(e)}"
