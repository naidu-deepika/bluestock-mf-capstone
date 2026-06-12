"""
Master Pipeline Script
Bluestock Fintech - Mutual Fund Analytics Capstone
Run this script to execute the complete ETL pipeline
"""

import subprocess
import sys

def run_script(script_path):
    print(f"\nRunning {script_path}...")
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ {script_path} completed successfully")
    else:
        print(f"❌ {script_path} failed")
        print(result.stderr)

if __name__ == "__main__":
    print("Starting Bluestock MF Capstone Pipeline...")
    run_script("scripts/live_nav_fetch.py")
    run_script("scripts/etl_pipeline.py")
    run_script("scripts/recommender.py")
    print("\n Pipeline complete!")