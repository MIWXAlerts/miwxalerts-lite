import requests
import datetime
from colorama import Fore, Style, init

init(autoreset=True)


STATES = ["MI", "WI", "OH", "IL", "IN"]
STATE_QUERY = ",".join(STATES)

API_URL = f"https://api.weather.gov/alerts/active?area={STATE_QUERY}"
USER_AGENT = "glsn-lite/1.0 (Great Lakes Severe Network)"



def color_for_severity(severity):
    severity = (severity or "").lower()
    if severity == "extreme":
        return Fore.MAGENTA
    elif severity == "severe":
        return Fore.RED
    elif severity == "moderate":
        return Fore.YELLOW
    elif severity == "minor":
        return Fore.GREEN
    return Fore.WHITE


def emoji_for_event(event):
    e = (event or "").lower()
    if "tornado" in e:
        return "🌪️"
    if "thunderstorm" in e:
        return "⛈️"
    if "flood" in e:
        return "🌊"
    if "winter" in e or "snow" in e or "ice" in e:
        return "❄️"
    if "heat" in e:
        return "🔥"
    if "wind" in e:
        return "💨"
    if "fog" in e:
        return "🌫️"
    return "⚠️"



def severe_tags(props):
    desc = (props.get("description") or "").lower()
    tags = []

    if "tornado emergency" in desc:
        tags.append("EMERGENCY")
    if "particularly dangerous situation" in desc or "pds" in desc:
        tags.append("PDS")
    if "observed tornado" in desc or "confirmed tornado" in desc:
        tags.append("OBSERVED")
    if "destructive" in desc:
        tags.append("DESTRUCTIVE")

    return tags


def winter_tags(event):
    e = (event or "").lower()
    tags = []

    if "blizzard" in e:
        tags.append("BLIZZARD")
    if "snow squall" in e:
        tags.append("SNOW SQUALL")
    if "ice storm" in e:
        tags.append("ICE")
    if "freezing rain" in e:
        tags.append("FREEZING RAIN")
    if "winter storm" in e:
        tags.append("WINTER STORM")

    return tags


def fetch_alerts():
    try:
        response = requests.get(
            API_URL,
            headers={"User-Agent": USER_AGENT},
            timeout=15
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"{Fore.RED}Error fetching alerts:{Style.RESET_ALL} {e}")
        return None


def display_alerts(data):
    if not data or "features" not in data:
        print(f"{Fore.YELLOW}No data available.{Style.RESET_ALL}")
        return

    alerts = data["features"]
    if not alerts:
        print(
            f"{Fore.GREEN}✅ No active alerts across the Great Lakes region."
            f"{Style.RESET_ALL}"
        )
        return

    print(
        f"{Fore.CYAN}⚠️ Active Weather Alerts — Great Lakes Severe Network"
        f"{Style.RESET_ALL}\n"
    )

    state_buckets = {state: [] for state in STATES}


    for alert in alerts:
        props = alert.get("properties", {})
        area = (props.get("areaDesc") or "").upper()

        for state in STATES:
            if f", {state}" in area or area.endswith(f" {state}"):
                state_buckets[state].append(alert)


    for state in STATES:
        state_alerts = state_buckets[state]
        if not state_alerts:
            continue

        print(f"{Fore.BLUE}📍 {state} — {len(state_alerts)} alert(s){Style.RESET_ALL}")
        print("=" * 60)

        for alert in state_alerts:
            props = alert.get("properties", {})

            event = props.get("event", "Unknown Event")
            severity = props.get("severity", "Unknown")
            area = props.get("areaDesc", "Unknown area")
            effective = props.get("effective", "N/A")
            expires = props.get("expires", "N/A")
            headline = props.get("headline", "No headline")
            status = props.get("status", "Actual")
            sender = props.get("senderName", "NWS")

            sev_color = color_for_severity(severity)
            emoji = emoji_for_event(event)

            tags = []
            if "tornado" in event.lower():
                tags.extend(severe_tags(props))
            if any(x in event.lower() for x in ["winter", "snow", "ice"]):
                tags.extend(winter_tags(event))

            tag_str = f" [{' | '.join(tags)}]" if tags else ""

            print(f"{sev_color}{emoji} {event} ({severity}){tag_str}{Style.RESET_ALL}")
            print(f"   {headline}")
            print(f"   Areas: {area}")
            print(f"   Issued by: {sender}")
            print(f"   Status: {status}")
            print(f"   Effective: {effective}")
            print(f"   Expires:   {expires}")
            print("-" * 60)

    print(
        f"\nLast updated: "
        f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )



if __name__ == "__main__":
    data = fetch_alerts()
    display_alerts(data)