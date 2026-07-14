import json
import requests
import sys

# User-provided payload
payload = {
    "events": [
        {
            "event": "EDBFEBHDDAI",
            "program": "vf8dN49jprI",
            "programStage": "aKclf7Yl1PE",
            "orgUnit": "QDc7Wijvfca",
            "eventDate": "2026-06-01",
            "attributeCategoryOptions": "14UMmqvSBe5",
            "attributeOptionCombo": "Lf2Axb9E6B4",
            "status": "COMPLETED",
            "dataValues": [
                {
                    "dataElement": "AJAraEcfH63",
                    "value": "No"
                },
                {
                    "dataElement": "C8n6hBilwsX",
                    "value": "R99"
                },
                {
                    "dataElement": "dsiwvNQLe5n",
                    "value": "KANSANGA"
                },
                {
                    "dataElement": "dTd7txVzhgY",
                    "value": "R99"
                },
                {
                    "dataElement": "e96GB4CXyd3",
                    "value": "Female"
                },
                {
                    "dataElement": "FGagV1Utrdh",
                    "value": "UG-VXP-964"
                },
                {
                    "dataElement": "FhHPxY16vet",
                    "value": "true"
                },
                {
                    "dataElement": "i8rrl8YWxLF",
                    "value": "2026-05-25T11:27:00"
                },
                {
                    "dataElement": "KpfvNQSsWIw",
                    "value": "Unknown"
                },
                {
                    "dataElement": "MOstDqSY0gO",
                    "value": "0747640720"
                },
                {
                    "dataElement": "PaoRZbokFWJ",
                    "value": "EMR System"
                },
                {
                    "dataElement": "q7e7FOXKnOf",
                    "value": 0
                },
                {
                    "dataElement": "QGFYJK00ES7",
                    "value": "Unknown contributing cause"
                },
                {
                    "dataElement": "QTKk2Xt8KDu",
                    "value": "Unknown contributing cause"
                },
                {
                    "dataElement": "RbrUuKFSqkZ",
                    "value": "2026-04-28"
                },
                {
                    "dataElement": "sfpqAeqKeyQ",
                    "value": "Meningitis, unspecified"
                },
                {
                    "dataElement": "tuMMQsGtE69",
                    "value": "R99"
                },
                {
                    "dataElement": "twVlVWM3ffz",
                    "value": "Approved"
                },
                {
                    "dataElement": "xNCSFrgdUgi",
                    "value": "NAGURU HOSPITAL"
                },
                {
                    "dataElement": "ymyLrfEcYkD",
                    "value": 0
                },
                {
                    "dataElement": "Z41di0TRjIu",
                    "value": "Health Facility"
                },
                {
                    "dataElement": "zb7uTuBCPrN",
                    "value": "Unknown antecedent cause"
                },
                {
                    "dataElement": "zcn7acUB6x1",
                    "value": "No"
                },
                {
                    "dataElement": "zD0E77W4rFs",
                    "value": "G03.9"
                },
                {
                    "dataElement": "ZKBE8Xm9DJG",
                    "value": "292"
                },
                {
                    "dataElement": "ZYKmQ9GPOaF",
                    "value": "AMYRA NANYOMBI"
                }
            ]
        },
        {
            "event": "EFADDABDHCD",
            "program": "vf8dN49jprI",
            "programStage": "aKclf7Yl1PE",
            "orgUnit": "QDc7Wijvfca",
            "eventDate": "2026-06-01",
            "attributeCategoryOptions": "14UMmqvSBe5",
            "attributeOptionCombo": "Lf2Axb9E6B4",
            "status": "COMPLETED",
            "dataValues": [
                {
                    "dataElement": "AJAraEcfH63",
                    "value": "No"
                },
                {
                    "dataElement": "C8n6hBilwsX",
                    "value": "R99"
                },
                {
                    "dataElement": "dsiwvNQLe5n",
                    "value": "KITUKUTWE"
                },
                {
                    "dataElement": "dTd7txVzhgY",
                    "value": "R99"
                },
                {
                    "dataElement": "e96GB4CXyd3",
                    "value": "Male"
                },
                {
                    "dataElement": "FGagV1Utrdh",
                    "value": "UG-GMY-518"
                },
                {
                    "dataElement": "FhHPxY16vet",
                    "value": "true"
                },
                {
                    "dataElement": "i8rrl8YWxLF",
                    "value": "2026-05-28T01:30:00"
                },
                {
                    "dataElement": "KpfvNQSsWIw",
                    "value": "Unknown"
                },
                {
                    "dataElement": "MOstDqSY0gO",
                    "value": "HHWYBY2NHJHH"
                },
                {
                    "dataElement": "PaoRZbokFWJ",
                    "value": "EMR System"
                },
                {
                    "dataElement": "q7e7FOXKnOf",
                    "value": 3
                },
                {
                    "dataElement": "QGFYJK00ES7",
                    "value": "Unknown contributing cause"
                },
                {
                    "dataElement": "QTKk2Xt8KDu",
                    "value": "Unknown contributing cause"
                },
                {
                    "dataElement": "RbrUuKFSqkZ",
                    "value": "2023-04-12"
                },
                {
                    "dataElement": "sfpqAeqKeyQ",
                    "value": "Other severe and complicated Plasmodium falciparum malaria"
                },
                {
                    "dataElement": "tuMMQsGtE69",
                    "value": "R99"
                },
                {
                    "dataElement": "twVlVWM3ffz",
                    "value": "Approved"
                },
                {
                    "dataElement": "xNCSFrgdUgi",
                    "value": "NAGURU HOSPITAL"
                },
                {
                    "dataElement": "ymyLrfEcYkD",
                    "value": 0
                },
                {
                    "dataElement": "Z41di0TRjIu",
                    "value": "Health Facility"
                },
                {
                    "dataElement": "zb7uTuBCPrN",
                    "value": "Unknown antecedent cause"
                },
                {
                    "dataElement": "zcn7acUB6x1",
                    "value": "No"
                },
                {
                    "dataElement": "zD0E77W4rFs",
                    "value": "B50.8"
                },
                {
                    "dataElement": "ZKBE8Xm9DJG",
                    "value": "293"
                },
                {
                    "dataElement": "ZYKmQ9GPOaF",
                    "value": "RYAN MBOGO"
                }
            ]
        },
        {
            "event": "EEDECFBHDGI",
            "program": "vf8dN49jprI",
            "programStage": "aKclf7Yl1PE",
            "orgUnit": "QDc7Wijvfca",
            "eventDate": "2026-06-01",
            "attributeCategoryOptions": "14UMmqvSBe5",
            "attributeOptionCombo": "Lf2Axb9E6B4",
            "status": "COMPLETED",
            "dataValues": [
                {
                    "dataElement": "AJAraEcfH63",
                    "value": "No"
                },
                {
                    "dataElement": "C8n6hBilwsX",
                    "value": "R99"
                },
                {
                    "dataElement": "dsiwvNQLe5n",
                    "value": "BUKOTO"
                },
                {
                    "dataElement": "dTd7txVzhgY",
                    "value": "R99"
                },
                {
                    "dataElement": "e96GB4CXyd3",
                    "value": "Male"
                },
                {
                    "dataElement": "FGagV1Utrdh",
                    "value": "UG-KHB-369"
                },
                {
                    "dataElement": "FhHPxY16vet",
                    "value": "true"
                },
                {
                    "dataElement": "i8rrl8YWxLF",
                    "value": "2026-05-29T11:00:00"
                },
                {
                    "dataElement": "KpfvNQSsWIw",
                    "value": "Unknown"
                },
                {
                    "dataElement": "MOstDqSY0gO",
                    "value": "0758821125"
                },
                {
                    "dataElement": "PaoRZbokFWJ",
                    "value": "EMR System"
                },
                {
                    "dataElement": "q7e7FOXKnOf",
                    "value": 0
                },
                {
                    "dataElement": "QGFYJK00ES7",
                    "value": "Unknown contributing cause"
                },
                {
                    "dataElement": "QTKk2Xt8KDu",
                    "value": "Unknown contributing cause"
                },
                {
                    "dataElement": "RbrUuKFSqkZ",
                    "value": "2026-05-17"
                },
                {
                    "dataElement": "sfpqAeqKeyQ",
                    "value": "Sepsis of fetus or newborn"
                },
                {
                    "dataElement": "tuMMQsGtE69",
                    "value": "R99"
                },
                {
                    "dataElement": "twVlVWM3ffz",
                    "value": "Approved"
                },
                {
                    "dataElement": "xNCSFrgdUgi",
                    "value": "NAGURU HOSPITAL"
                },
                {
                    "dataElement": "ymyLrfEcYkD",
                    "value": 0
                },
                {
                    "dataElement": "Z41di0TRjIu",
                    "value": "Health Facility"
                },
                {
                    "dataElement": "zb7uTuBCPrN",
                    "value": "Unknown antecedent cause"
                },
                {
                    "dataElement": "zcn7acUB6x1",
                    "value": "No"
                },
                {
                    "dataElement": "zD0E77W4rFs",
                    "value": "KA60"
                },
                {
                    "dataElement": "ZKBE8Xm9DJG",
                    "value": "294"
                },
                {
                    "dataElement": "ZYKmQ9GPOaF",
                    "value": "ADAN AYAMBA"
                }
            ]
        },
        {
            "event": "EJHHIDFDCBJ",
            "program": "vf8dN49jprI",
            "programStage": "aKclf7Yl1PE",
            "orgUnit": "QDc7Wijvfca",
            "eventDate": "2026-06-01",
            "attributeCategoryOptions": "14UMmqvSBe5",
            "attributeOptionCombo": "Lf2Axb9E6B4",
            "status": "COMPLETED",
            "dataValues": [
                {
                    "dataElement": "AJAraEcfH63",
                    "value": "No"
                },
                {
                    "dataElement": "C8n6hBilwsX",
                    "value": "R99"
                },
                {
                    "dataElement": "dsiwvNQLe5n",
                    "value": "BANDA"
                },
                {
                    "dataElement": "dTd7txVzhgY",
                    "value": "R99"
                },
                {
                    "dataElement": "e96GB4CXyd3",
                    "value": "Female"
                },
                {
                    "dataElement": "FGagV1Utrdh",
                    "value": "UG-TGB-284"
                },
                {
                    "dataElement": "FhHPxY16vet",
                    "value": "true"
                },
                {
                    "dataElement": "i8rrl8YWxLF",
                    "value": "2026-06-30T08:40:00"
                },
                {
                    "dataElement": "KpfvNQSsWIw",
                    "value": "Unknown"
                },
                {
                    "dataElement": "MOstDqSY0gO",
                    "value": "0002356"
                },
                {
                    "dataElement": "PaoRZbokFWJ",
                    "value": "EMR System"
                },
                {
                    "dataElement": "q7e7FOXKnOf",
                    "value": 1
                },
                {
                    "dataElement": "QGFYJK00ES7",
                    "value": "Unknown contributing cause"
                },
                {
                    "dataElement": "QTKk2Xt8KDu",
                    "value": "Unknown contributing cause"
                },
                {
                    "dataElement": "RbrUuKFSqkZ",
                    "value": "2024-10-11"
                },
                {
                    "dataElement": "sfpqAeqKeyQ",
                    "value": "Bacterial pneumonia, unspecified"
                },
                {
                    "dataElement": "tuMMQsGtE69",
                    "value": "R99"
                },
                {
                    "dataElement": "twVlVWM3ffz",
                    "value": "Approved"
                },
                {
                    "dataElement": "xNCSFrgdUgi",
                    "value": "NAGURU HOSPITAL"
                },
                {
                    "dataElement": "ymyLrfEcYkD",
                    "value": 0
                },
                {
                    "dataElement": "Z41di0TRjIu",
                    "value": "Health Facility"
                },
                {
                    "dataElement": "zb7uTuBCPrN",
                    "value": "Unknown antecedent cause"
                },
                {
                    "dataElement": "zcn7acUB6x1",
                    "value": "No"
                },
                {
                    "dataElement": "zD0E77W4rFs",
                    "value": "J15.9"
                },
                {
                    "dataElement": "ZKBE8Xm9DJG",
                    "value": "296"
                },
                {
                    "dataElement": "ZYKmQ9GPOaF",
                    "value": "PHOEBE NANTAMBI"
                }
            ]
        },
        {
            "event": "EFEJFCCIJCD",
            "program": "vf8dN49jprI",
            "programStage": "aKclf7Yl1PE",
            "orgUnit": "QDc7Wijvfca",
            "eventDate": "2026-06-06",
            "attributeCategoryOptions": "14UMmqvSBe5",
            "attributeOptionCombo": "Lf2Axb9E6B4",
            "status": "COMPLETED",
            "dataValues": [
                {
                    "dataElement": "AJAraEcfH63",
                    "value": "No"
                },
                {
                    "dataElement": "C8n6hBilwsX",
                    "value": "XY7Z"
                },
                {
                    "dataElement": "dsiwvNQLe5n",
                    "value": "dfghjk"
                },
                {
                    "dataElement": "dTd7txVzhgY",
                    "value": "XY7Z"
                },
                {
                    "dataElement": "e96GB4CXyd3",
                    "value": "Female"
                },
                {
                    "dataElement": "FGagV1Utrdh",
                    "value": "UG-UBB-642"
                },
                {
                    "dataElement": "FhHPxY16vet",
                    "value": "true"
                },
                {
                    "dataElement": "i8rrl8YWxLF",
                    "value": "2026-06-06T22:37:00"
                },
                {
                    "dataElement": "KpfvNQSsWIw",
                    "value": "Unknown"
                },
                {
                    "dataElement": "MOstDqSY0gO",
                    "value": "34567890456"
                },
                {
                    "dataElement": "PaoRZbokFWJ",
                    "value": "EMR System"
                },
                {
                    "dataElement": "q7e7FOXKnOf",
                    "value": 21
                },
                {
                    "dataElement": "QGFYJK00ES7",
                    "value": "Provisional diagnosis"
                },
                {
                    "dataElement": "QTKk2Xt8KDu",
                    "value": "Provisional diagnosis"
                },
                {
                    "dataElement": "RbrUuKFSqkZ",
                    "value": "2005-01-01"
                },
                {
                    "dataElement": "sfpqAeqKeyQ",
                    "value": "Chronic"
                },
                {
                    "dataElement": "tuMMQsGtE69",
                    "value": "XS43"
                },
                {
                    "dataElement": "twVlVWM3ffz",
                    "value": "Approved"
                },
                {
                    "dataElement": "xNCSFrgdUgi",
                    "value": "Nagulu"
                },
                {
                    "dataElement": "ymyLrfEcYkD",
                    "value": 0
                },
                {
                    "dataElement": "Z41di0TRjIu",
                    "value": "Health Facility"
                },
                {
                    "dataElement": "zb7uTuBCPrN",
                    "value": "Normal weight BMI 18.5 24.9"
                },
                {
                    "dataElement": "zcn7acUB6x1",
                    "value": "No"
                },
                {
                    "dataElement": "zD0E77W4rFs",
                    "value": "XT8W"
                },
                {
                    "dataElement": "ZKBE8Xm9DJG",
                    "value": "303"
                },
                {
                    "dataElement": "ZYKmQ9GPOaF",
                    "value": "Test1 Testfp"
                }
            ]
        }
    ]
}

# The target url and credentials from the user request
target_url = "https://hmis-tests.health.go.ug/api/40/events"
auth = ("mccod.test", "Dhis2@2025")
headers = {
    "Content-Type": "application/json"
}

# Also try base path /api/events if api/40/events fails, but let's start with api/40/events first
try:
    print(f"Posting {len(payload['events'])} events to {target_url}...")
    response = requests.post(target_url, json=payload, headers=headers, auth=auth, timeout=30)
    print(f"Response status code: {response.status_code}")
    print("Response text:")
    try:
        print(json.dumps(response.json(), indent=2))
    except Exception:
        print(response.text)
        
except Exception as e:
    print(f"An error occurred while posting: {e}")
    sys.exit(1)
