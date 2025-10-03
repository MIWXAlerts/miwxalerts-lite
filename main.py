import requests
import datetime

API_URL = "https://api.weather.gov/alerts/active?area=MI"

def fetch_alerts():
    try:
        response = requests.get(API_URL, headers={"User-Agent": "MIWXAlerts OpenSource"})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching alerts: {e}")
        return None

def display_alerts(data):
    if not data or "features" not in data:
        print("No data available.")
        return
    
    alerts = data["features"]
    if not alerts:
        print("✅ No active alerts in Michigan.")
        return

    print(f"⚠️ Active Weather Alerts for Michigan ({len(alerts)} total):\n")

    for alert in alerts:
        props = alert["properties"]
        headline = props.get("headline", "No headline")
        event = props.get("event", "Unknown Event")
        severity = props.get("severity", "Unknown")
        area = props.get("areaDesc", "Unknown area")
        effective = props.get("effective", "N/A")
        expires = props.get("expires", "N/A")

        print(f"🔹 {event} ({severity})")
        print(f"   {headline}")
        print(f"   Areas: {area}")
        print(f"   Effective: {effective}")
        print(f"   Expires:   {expires}")
        print("-" * 60)

if __name__ == "__main__":
    data = fetch_alerts()
    display_alerts(data)
