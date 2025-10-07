import requests
import datetime
from colorama import Fore, Style, init


init(autoreset=True)

API_URL = "https://api.weather.gov/alerts/active?area=MI"


def color_for_severity(severity):
    """ Returns color based on severity level. """
    severity = severity.lower()
    if severity == "extreme":
        return Fore.MAGENTA
    elif severity == "severe":
        return Fore.RED
    elif severity == "moderate":
        return Fore.YELLOW
    elif severity == "minor":
        return Fore.GREEN
    else:
        return Fore.WHITE

def fetch_alerts():
    """Fetch active alerts from NWS for Michigan."""
    try:
        response = requests.get(API_URL, headers={"User-Agent": "MIWXAlerts OpenSource"})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"{Fore.RED}Error fetching alerts:{Style.RESET_ALL} {e}")
        return None

def display_alerts(data):
    """Display alert data with color-coded severity and formatted output."""
    if not data or "features" not in data:
        print(f"{Fore.YELLOW}No data available.{Style.RESET_ALL}")
        return
    
    alerts = data["features"]
    if not alerts:
        print(f"{Fore.GREEN}✅ No active alerts in Michigan.{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}⚠️ Active Weather Alerts for Michigan ({len(alerts)} total):{Style.RESET_ALL}\n")

    for alert in alerts:
        props = alert["properties"]
        headline = props.get("headline", "No headline")
        event = props.get("event", "Unknown Event")
        severity = props.get("severity", "Unknown")
        area = props.get("areaDesc", "Unknown area")
        effective = props.get("effective", "N/A")
        expires = props.get("expires", "N/A")

        sev_color = color_for_severity(severity)

        print(f"{sev_color}🔹 {event} ({severity}){Style.RESET_ALL}")
        print(f"   {headline}")
        print(f"   Areas: {area}")
        print(f"   Effective: {effective}")
        print(f"   Expires:   {expires}")
        print("-" * 60)

    print(f"\nLast updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    data = fetch_alerts()
    display_alerts(data)
