import json
import requests
import sys

payload_path = r"C:\Users\SK\Downloads\correct_dhis2_payload.json"
url = "https://hmis-tests.health.go.ug/api/40/events"
auth = ("mccod.test", "Dhis2@2025")

try:
    with open(payload_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    print(f"Loaded payload from {payload_path}")
    print(f"Data type: {type(data)}")
    
    events_list = []
    if isinstance(data, list):
        events_list = data
    elif isinstance(data, dict) and "events" in data:
        events_list = data["events"]
    else:
        print("Error: Unknown structure of payload.")
        sys.exit(1)
        
    # Inject attributeOptionCombo into every event
    for event in events_list:
        if "attributeOptionCombo" not in event or not event["attributeOptionCombo"]:
            event["attributeOptionCombo"] = "Lf2Axb9E6B4"
            
    post_payload = {"events": events_list}
    print(f"Prepared {len(events_list)} events with attributeOptionCombo.")
        
    headers = {
        "Content-Type": "application/json"
    }
    
    print(f"Posting to {url}...")
    response = requests.post(url, json=post_payload, headers=headers, auth=auth, timeout=60)
    
    print(f"Status Code: {response.status_code}")
    print("Response Content:")
    try:
        # Pretty print response if it's JSON
        print(json.dumps(response.json(), indent=2))
    except Exception:
        print(response.text)
        
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
