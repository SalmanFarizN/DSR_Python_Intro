#!/usr/bin/env python3
"""
Download datasets for the DSR Python, NumPy and Pandas course.

This script downloads:
1. Titanic dataset - classic dataset for data science teaching
2. Bike share dataset - for time series and real-world analysis

Run from repo root: python data/download_data.py
"""

import os
import urllib.request
import csv
from datetime import datetime, timedelta
import random

DATA_DIR = os.path.dirname(os.path.abspath(__file__))


def download_file(url, filepath, description):
    """Download a file if it doesn't already exist."""
    if os.path.exists(filepath):
        print(f"✓ {description} already exists, skipping download")
        return True
    
    print(f"⬇ Downloading {description}...")
    try:
        urllib.request.urlretrieve(url, filepath)
        print(f"✓ Saved to {filepath}")
        return True
    except Exception as e:
        print(f"✗ Error downloading {description}: {e}")
        return False


def download_titanic():
    """Download the Titanic dataset."""
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    filepath = os.path.join(DATA_DIR, "titanic.csv")
    return download_file(url, filepath, "Titanic dataset")


def generate_bikes_data():
    """Generate realistic bike share data for Berlin simulation."""
    filepath = os.path.join(DATA_DIR, "berlin_bikes.csv")
    
    if os.path.exists(filepath):
        print("✓ Berlin bikes dataset already exists, skipping generation")
        return True
    
    print("⚙ Generating Berlin bike share dataset...")
    
    try:
        # Berlin-style station names
        stations = [
            ("31001", "Alexanderplatz"),
            ("31002", "Brandenburger Tor"),
            ("31003", "Potsdamer Platz"),
            ("31004", "Friedrichstraße"),
            ("31005", "Hackescher Markt"),
            ("31006", "Warschauer Straße"),
            ("31007", "Kottbusser Tor"),
            ("31008", "Zoologischer Garten"),
            ("31009", "Hauptbahnhof"),
            ("31010", "Prenzlauer Berg"),
            ("31011", "Kreuzberg"),
            ("31012", "Neukölln"),
            ("31013", "Charlottenburg"),
            ("31014", "Mitte"),
            ("31015", "Schöneberg"),
            ("31016", "Tiergarten"),
            ("31017", "Wedding"),
            ("31018", "Friedrichshain"),
            ("31019", "Tempelhof"),
            ("31020", "Steglitz"),
        ]
        
        random.seed(42)  # For reproducibility
        
        # Generate trips for 3 months
        start_date = datetime(2019, 1, 1)
        end_date = datetime(2019, 3, 31)
        
        rows = []
        bike_ids = [f"B{i:04d}" for i in range(1, 501)]  # 500 bikes
        
        current_date = start_date
        while current_date <= end_date:
            # More trips on weekdays during commute hours
            is_weekend = current_date.weekday() >= 5
            
            # Generate trips for this day
            if is_weekend:
                num_trips = random.randint(200, 400)
            else:
                num_trips = random.randint(400, 700)
            
            for _ in range(num_trips):
                # Hour distribution (commute peaks on weekdays)
                if is_weekend:
                    hour = random.choices(
                        range(24),
                        weights=[1,1,1,1,1,2,3,4,5,6,7,8,8,8,7,6,6,5,5,4,3,2,1,1]
                    )[0]
                else:
                    hour = random.choices(
                        range(24),
                        weights=[1,1,1,1,2,4,8,12,15,10,6,5,5,5,5,6,8,12,10,6,4,3,2,1]
                    )[0]
                
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                
                trip_start = current_date.replace(hour=hour, minute=minute, second=second)
                
                # Duration: casual users take longer trips
                user_type = random.choices(
                    ["Member", "Casual"],
                    weights=[70, 30]
                )[0]
                
                if user_type == "Member":
                    duration = int(random.gauss(600, 200))  # ~10 min avg
                else:
                    duration = int(random.gauss(1200, 400))  # ~20 min avg
                
                duration = max(60, min(duration, 7200))  # 1 min to 2 hours
                
                trip_end = trip_start + timedelta(seconds=duration)
                
                # Random stations
                start_station = random.choice(stations)
                end_station = random.choice(stations)
                
                bike_id = random.choice(bike_ids)
                
                rows.append({
                    'duration': duration,
                    'start_time': trip_start.strftime('%Y-%m-%d %H:%M:%S'),
                    'end_time': trip_end.strftime('%Y-%m-%d %H:%M:%S'),
                    'start_station_id': start_station[0],
                    'start_station': start_station[1],
                    'end_station_id': end_station[0],
                    'end_station': end_station[1],
                    'bike_id': bike_id,
                    'user_type': user_type
                })
            
            current_date += timedelta(days=1)
        
        # Write to CSV
        fieldnames = ['duration', 'start_time', 'end_time', 'start_station_id', 
                     'start_station', 'end_station_id', 'end_station', 'bike_id', 'user_type']
        
        with open(filepath, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        print(f"✓ Generated Berlin bikes dataset: {filepath}")
        print(f"  ({len(rows):,} records, {start_date.date()} to {end_date.date()})")
        return True
        
    except Exception as e:
        print(f"✗ Error generating bike data: {e}")
        return False


def main():
    """Download/generate all datasets."""
    print("=" * 60)
    print("DSR Python Course - Dataset Downloader")
    print("=" * 60)
    print()
    
    success = True
    
    # Download Titanic
    if not download_titanic():
        success = False
    
    # Generate bike data
    if not generate_bikes_data():
        success = False
    
    print()
    print("=" * 60)
    if success:
        print("✓ All datasets ready!")
    else:
        print("⚠ Some operations failed. Check the errors above.")
    print("=" * 60)
    
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
