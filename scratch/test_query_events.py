import requests
import json

server_url = "https://hmis-tests.health.go.ug"
auth = ("mccod.test", "Dhis2@2025")
headers = {
    "Accept": "application/json"
}

program = "vf8dN49jprI"

# Query the events endpoint with filters
# Let's search by Case Number / ID: ZKBE8Xm9DJG is 292
case_number = "292"
url = f"{server_url}/api/events.json?program={program}&ouMode=ALL&pageSize=5"

print(f"GET: {url}")
try:
    res = requests.get(url, auth=auth, headers=headers, timeout=20)
    print(f"Status Code: {res.status_code}")
    if res.status_code == 200:
        data = res.json()
        events = data.get("events", [])
        print(f"Found {len(events)} events.")
        print(json.dumps(events, indent=2))
    else:
        print(f"Response: {res.text}")
except Exception as e:
    print(f"Error: {e}")
