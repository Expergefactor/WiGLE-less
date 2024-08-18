import folium
import pandas as pd
from geopy.distance import geodesic
import os
import re
import subprocess

map_html_path = os.path.join('files', 'Maps', 'manually_created')
if not os.path.exists(map_html_path):
    os.makedirs(map_html_path)


def banner():
    print(
        """\033[1;94m
        *******************************************************************
        
                    ███    ███  █████  ██████      ██ ████████ 
                    ████  ████ ██   ██ ██   ██     ██    ██    
                    ██ ████ ██ ███████ ██████      ██    ██    
                    ██  ██  ██ ██   ██ ██          ██    ██    
                    ██      ██ ██   ██ ██          ██    ██ 
                    
        *******************************************************************
    \033[0m""")


def get_next_file_number(directory, base_filename):
    pattern = re.compile(rf'{re.escape(base_filename)}_(\d+)\.html')
    existing_files = os.listdir(directory)
    numbers = []

    for filename in existing_files:
        match = pattern.match(filename)
        if match:
            numbers.append(int(match.group(1)))

    next_number = max(numbers, default=0) + 1
    return next_number


def create_route_map(input_csv_filename):
    csv_file_path = os.path.join(f'files/DB_files/{input_csv_filename}.csv')

    try:
        df = pd.read_csv(csv_file_path, skiprows=1, usecols=['CurrentLatitude', 'CurrentLongitude'],
                         on_bad_lines='warn')
    except Exception as e:
        print(f"\033[1;91m Error reading CSV file: {e}\033[0m")
        return

    df['CurrentLatitude'] = pd.to_numeric(df['CurrentLatitude'], errors='coerce')
    df['CurrentLongitude'] = pd.to_numeric(df['CurrentLongitude'], errors='coerce')

    initial_count = len(df)

    df.dropna(subset=['CurrentLatitude', 'CurrentLongitude'], inplace=True)

    final_count = len(df)

    if df.empty:
        print("\033[1;91m Error: No valid data available after cleaning.\033[0m")
        return

    start_coords = (df['CurrentLatitude'].iloc[0], df['CurrentLongitude'].iloc[0])
    m = folium.Map(location=start_coords, zoom_start=6)

    points = []
    last_coords = None

    for i, row in df.iterrows():
        coords = (row['CurrentLatitude'], row['CurrentLongitude'])

        if last_coords is not None:
            try:
                distance = geodesic(last_coords, coords).meters
                if distance > 150:
                    if points:
                        folium.PolyLine(points, color='blue', weight=2.5).add_to(m)
                        points = []
                    print(f" GPS gap detected at row {i}, splitting route...")
            except Exception as e:
                print(f"\033[1;91m Error calculating distance at row {i}: {e}\033[0m")
                continue

        points.append(coords)
        last_coords = coords

    print(f"\n\033[1;92m Success!\n"
          f" Records read:                  {initial_count}\n"
          f" Records sent to map:           {final_count}"
          )
    difference = initial_count - final_count
    print(f" Records removed from map:      {difference}\033[0m")

    if points:
        folium.PolyLine(points, color='blue', weight=2.5).add_to(m)

    base_filename = f'Map'
    next_number = get_next_file_number('files/Maps/manually_created', base_filename)
    map_html_filename = f'{map_html_path}/{base_filename}_{next_number}.html'

    try:
        m.save(map_html_filename)
        print(f'\n\033[1;92m Map saved to\n\033[1;97m {map_html_filename}\n\033[0m')
    except Exception as e:
        print(f"\033[1;91m Error saving map: {e}\033[0m")


if __name__ == "__main__":
    banner()
    print("\033[1;97m * The input CSV file must be in the 'files/DB_files/' folder.\n"
          " * Do not use extension details (.csv).\033[0m\n")
    input_csv_filename = input("\033[1;93m Enter the CSV filename: \033[0m")
    create_route_map(input_csv_filename)
    try:
        while True:
            action = input("\n\033[1;93m Press 'enter' to return to the menu: \033[0m").strip().lower()
            if action == '':
                command = f"python3 menu.py"
                subprocess.run(command, shell=True)
                break
    except KeyboardInterrupt:
        exit(0)
