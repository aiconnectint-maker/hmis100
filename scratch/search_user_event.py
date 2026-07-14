import requests
import json
import sys

# Test server connection details
server_url = "https://hmis-tests.health.go.ug"
auth = ("hisp.skununka", "Aiconnect@123$")
headers = {
    "Accept": "application/json"
}

# The event IDs we posted
event_ids = [
    "EDBFEBHDDAI",
    "EFADDABDHCD",
    "EEDECFBHDGI",
    "EJHHIDFDCBJ",
    "EFEJFCCIJCD"
]

print("--- Checking Event IDs on hmis-tests ---")
for eid in event_ids:
    # Query specific event endpoint
    url = f"{server_url}/api/events/{eid}"
    print(f"\nGET: {url}")
    try:
        res = requests.get(url, auth=auth, headers=headers, timeout=15)
        if res.status_code == 200:
            data = res.json()
            print(f"FOUND EVENT: {eid}")
            print(f"  Program: {data.get('program')}")
            print(f"  OrgUnit: {data.get('orgUnit')} ({data.get('orgUnitName')})")
            print(f"  Event Date: {data.get('eventDate')}")
            print(f"  Status: {data.get('status')}")
            
            # Print a few key data values (like Name and Inpatient number)
            # ZYKmQ9GPOaF is Full Name, FGagV1Utrdh is Inpatient Number
            full_name = "N/A"
            inpatient_num = "N/A"
            for dv in data.get("dataValues", []):
                if dv.get("dataElement") == "ZYKmQ9GPOaF":
                    full_name = dv.get("value")
                elif dv.get("dataElement") == "FGagV1Utrdh":
                    inpatient_num = dv.get("value")
            
            print(f"  Patient Name: {full_name}")
            print(f"  Inpatient Number: {inpatient_num}")
        else:
            print(f"  Not Found or Error: Status code {res.status_code}")
            print(f"  Response: {res.text}")
    except Exception as e:
        print(f"  Request failed: {e}")
