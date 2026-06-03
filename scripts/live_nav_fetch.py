import requests
import pandas as pd
from pathlib import Path
import time

RAW = Path("data/raw")

schemes = {
    "125497": "HDFC_Top100",
    "119551": "SBI_Bluechip",
    "120503": "ICICI_Bluechip",
    "118632": "Nippon_LargeCap",
    "119092": "Axis_Bluechip",
    "120841": "Kotak_Bluechip",
}

for code, name in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    print(f"Fetching {name}...")
    
    for attempt in range(3):  # retry 3 times
        try:
            response = requests.get(url, timeout=30)
            data = response.json()
            df = pd.DataFrame(data["data"])
            df["amfi_code"] = code
            df["scheme_name"] = data["meta"]["scheme_name"]
            df.to_csv(RAW / f"live_nav_{name}.csv", index=False)
            print(f"Saved {len(df)} rows for {name}")
            break
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(5)

print("\n ALL LIVE NAV DATA FETCHED AND SAVED")