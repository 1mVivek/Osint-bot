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
    try:
        res = requests.get(f"https://breachdirectory.org/api/{email}", timeout=5)
        data = res.json()

        if data.get("success") == False:
            return "❌ Error or invalid email."

        if data.get("found") == False:
            return "✅ No breaches found for this email."

        breach_list = data.get("result", [])
        breach_names = [b.get("source", "Unknown") for b in breach_list]

        if not breach_names:
            return "⚠️ Breaches found, but details not available."

        return (
            f"⚠️ Breaches found ({len(breach_names)}):\n" +
            "\n".join(set(breach_names))
        )
    except Exception as e:
        return f"❌ Error checking email: {str(e)}"

# Placeholder for phone lookup (you can integrate NumVerify or Truecaller if needed)
def phone_lookup(number):
    return (
        f"🔍 Phone lookup for {number}:\n"
        f"(Real-time phone info requires integration with NumVerify or another service — not included here)"
    )
