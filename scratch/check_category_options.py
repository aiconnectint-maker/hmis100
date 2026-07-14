import requests
import json

server_url = "https://hmis-tests.health.go.ug"
auth = ("hisp.skununka", "Aiconnect@123$")
headers = {
    "Accept": "application/json"
}

# 1. Get Category Options
try:
    url = f"{server_url}/api/categoryOptions.json?paging=false&fields=id,displayName,code"
    res = requests.get(url, auth=auth, headers=headers, timeout=15)
    print(f"Category Options Status: {res.status_code}")
    if res.status_code == 200:
        options = res.json().get("categoryOptions", [])
        print(f"Found {len(options)} category options:")
        for opt in options[:20]:
            print(f"  {opt}")
        if len(options) > 20:
            print("  ...")
    else:
        print(res.text)
except Exception as e:
    print(f"Error: {e}")

# 2. Search specifically for l4UMmqvSBe5, 14UMmqvSBe5, VJU0bY182ND, and wUteK0Om3qP
for opt_id in ["l4UMmqvSBe5", "14UMmqvSBe5", "VJU0bY182ND", "wUteK0Om3qP"]:
    try:
        url = f"{server_url}/api/categoryOptions/{opt_id}.json"
        res = requests.get(url, auth=auth, headers=headers, timeout=15)
        print(f"Query {opt_id} Status: {res.status_code}")
        if res.status_code == 200:
            data = res.json()
            print(f"  Name: {data.get('displayName')}")
            print(f"  Access: {json.dumps(data.get('access'))}")
        else:
            print(res.text)
    except Exception as e:
        print(f"Error: {e}")
