import requests

server_url = "https://hmis-tests.health.go.ug"

creds = [
    ("mccod.test", "Dhis2@2025"),
    ("hisp.skununka", "Nomisr123$$$$"),
    ("hisp.skununka", "Aiconnect@123$"),
    ("hisp.colupot", "Baby77@Baby771"),
    ("admin", "Nomisr123$$$$")
]

for username, password in creds:
    url = f"{server_url}/api/me"
    try:
        res = requests.get(url, auth=(username, password), timeout=10)
        print(f"Testing {username} / {password} -> Status: {res.status_code}")
        if res.status_code == 200:
            print(f"  SUCCESS! User: {res.json().get('username')}")
    except Exception as e:
        print(f"  Error testing {username}: {e}")
