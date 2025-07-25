import requests
import os

# IP Lookup using ip-api.com (free and simple)
def ip_lookup(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        res.raise_for_status()
        data = res.json()

        if data.get('status') != 'success':
            return f"❌ Invalid IP or domain: {data.get('message', 'Unknown error')}"

        return (
            f"🌍 IP Info:\n"
            f"IP: {data.get('query')}\n"
            f"Country: {data.get('country')} ({data.get('countryCode')})\n"
            f"Region: {data.get('regionName')}\n"
            f"City: {data.get('city')}\n"
            f"ISP: {data.get('isp')}\n"
            f"Org: {data.get('org')}\n"
            f"Timezone: {data.get('timezone')}"
        )
    except Exception as e:
        return f"❌ Error fetching IP info: {str(e)}"

# Email breach lookup using HaveIBeenPwned
def email_breach_check(email):
    api_key = os.getenv("HIBP_API_KEY")
    if not api_key:
        return "⚠️ Email check disabled: HIBP API key not found in .env."

    try:
        headers = {
            "hibp-api-key": api_key,
            "User-Agent": "OSINT-Bot"  # Required by HIBP
        }

        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        res = requests.get(url, headers=headers, timeout=5)

        if res.status_code == 404:
            return "✅ No breaches found for this email!"
        elif res.status_code == 200:
            breaches = [b.get('Name') for b in res.json()]
            return f"⚠️ Breaches found ({len(breaches)}):\n" + "\n".join(breaches)
        elif res.status_code == 401:
            return "❌ Unauthorized: Invalid HIBP API key."
        elif res.status_code == 429:
            return "⏳ Rate limited. Please try again later."
        else:
            return f"❌ Unexpected error: HTTP {res.status_code}"
    except Exception as e:
        return f"❌ Error checking email: {str(e)}"

# Placeholder for phone lookup (you can integrate NumVerify or Truecaller if needed)
def phone_lookup(number):
    return (
        f"🔍 Phone lookup for {number}:\n"
        f"(Real-time phone info requires integration with NumVerify or another service — not included here)"
    )
