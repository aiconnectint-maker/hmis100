import csv
import json
import os
import sys

def clean_number(val):
    if not val:
        return None
    # Strip non-numeric helper characters, but keep numbers
    cleaned = ''.join(c for c in str(val) if c.isdigit() or c == '.')
    try:
        if '.' in cleaned:
            return float(cleaned)
        return int(cleaned)
    except ValueError:
        return None

def clean_pregnancy_status(val):
    val_upper = str(val).strip().upper()
    if val_upper in ["YES", "Y", "TRUE", "1"]:
        return "Yes"
    if val_upper in ["NO", "N", "FALSE", "0"]:
        return "No"
    return "Unknown"

def convert_csv_to_dhis2(csv_path, output_json_path):
    events = []
    
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}")
        return

    with open(csv_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # DHIS2 Event structure
            event = {
                "program": "vf8dN49jprI",
                "programStage": "aKclf7Yl1PE",
                "orgUnit": "BrtC10sqp45", # Default OrgUnit mapped in EMR JSON
                "eventDate": row.get("event_date_only") or row.get("event_timestamp", "").split(" ")[0] or "2026-07-01",
                "attributeOptionCombo": "Lf2Axb9E6B4",
                "status": "COMPLETED",
                "dataValues": []
            }
            
            # Include event UID if present in CSV
            event_uid = row.get("event_uid")
            if event_uid:
                event["event"] = event_uid
            
            # Helper to append valid values only
            def add_val(de, value):
                if value is not None and str(value).strip() != "":
                    event["dataValues"].append({"dataElement": de, "value": value})

            # Data Element Mappings
            add_val("ZYKmQ9GPOaF", row.get("full_name"))
            
            # ID number / NIN validation adjustment
            id_no = str(row.get("id_no") or "").strip()
            if id_no == "222" or not id_no:
                id_no = "NINNOTPROVIDED"
            add_val("MOstDqSY0gO", id_no)
            
            add_val("e96GB4CXyd3", row.get("gender"))
            add_val("RbrUuKFSqkZ", row.get("birth_date"))
            
            # Case Number mapping & formatting (must be at least 5 chars)
            case_no = str(row.get("moh_case_number") or "").strip()
            if not case_no:
                patient_id = row.get("patient_id") or row.get("source_id") or "UNKNOWN"
                case_no = f"EMR-CASE-{patient_id}"
            elif len(case_no) < 5:
                case_no = f"EMR-CASE-{case_no}"
            add_val("ZKBE8Xm9DJG", case_no)
            
            # Inpatient Number mapping
            add_val("FGagV1Utrdh", row.get("inpatient_number"))
            
            # Numeric Age
            age = clean_number(row.get("age_years"))
            if age is not None:
                add_val("q7e7FOXKnOf", age)
                
            # Date Time formats
            dt_death = row.get("time_of_death")
            if dt_death:
                # Format to DHIS2 standard: YYYY-MM-DDThh:mm:ss
                formatted_dt = dt_death.replace(" ", "T")
                add_val("i8rrl8YWxLF", formatted_dt)
            else:
                event_date = event["eventDate"]
                add_val("i8rrl8YWxLF", f"{event_date}T12:00:00")
                
            add_val("xNCSFrgdUgi", row.get("place_of_death"))
            add_val("dsiwvNQLe5n", row.get("occupation"))
            
            # Causes & ICD codes
            add_val("sfpqAeqKeyQ", row.get("cause_a_immediate"))
            add_val("zD0E77W4rFs", row.get("cause_a_icd"))
            
            # Numeric Time Intervals
            add_val("WkXxkKEJLsg", clean_number(row.get("intervalA"))) # Handled as numeric
            add_val("fleGy9CvHYh", clean_number(row.get("intervalB")))
            add_val("hO8No9fHVd2", clean_number(row.get("intervalC")))
            add_val("eCVDO6lt4go", clean_number(row.get("intervalD")))
            
            add_val("zb7uTuBCPrN", row.get("cause_b_antecedent"))
            add_val("tuMMQsGtE69", row.get("cause_b_icd"))
            add_val("QGFYJK00ES7", row.get("cause_c_other"))
            add_val("C8n6hBilwsX", row.get("cause_c_icd"))
            
            add_val("QTKk2Xt8KDu", row.get("final_underlying_cause_text"))
            add_val("dTd7txVzhgY", row.get("final_underlying_cause_code"))
            
            # Manner of Death (True Only)
            manner = str(row.get("manner_of_death", "")).strip().upper()
            if manner == "DISEASE":
                add_val("FhHPxY16vet", "true")
            elif manner == "ACCIDENT":
                add_val("gNM2Yhypydx", "true")
            elif manner == "ASSAULT":
                add_val("KsGOxFyzIs1", "true")
                
            # Mother/Pregnancy fields
            add_val("ymyLrfEcYkD", clean_number(row.get("parity")))
            add_val("K5BDPJQk1BP", row.get("delivery_mode"))
            add_val("Z41di0TRjIu", row.get("place_of_delivery"))
            
            add_val("zcn7acUB6x1", clean_pregnancy_status(row.get("pregnancy_related")))
            add_val("KpfvNQSsWIw", row.get("pregnancy_timing"))
            add_val("AJAraEcfH63", clean_pregnancy_status(row.get("pregnancy_contributed")))
            
            add_val("twVlVWM3ffz", row.get("approval_status"))
            add_val("PaoRZbokFWJ", row.get("examined_by"))
            
            events.append(event)
            
    # Write payload to file
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(events, f, indent=4)
        
    print(f"Successfully converted CSV records to DHIS2 payload: {output_json_path}")
    print(f"Converted {len(events)} events.")

if __name__ == "__main__":
    csv_in = r"C:\Users\SK\Downloads\cause_death_events_details.csv"
    json_out = r"C:\Users\SK\Downloads\correct_dhis2_payload.json"
    
    if len(sys.argv) > 1:
        csv_in = sys.argv[1]
    if len(sys.argv) > 2:
        json_out = sys.argv[2]
        
    convert_csv_to_dhis2(csv_in, json_out)
