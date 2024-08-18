import csv
import os
from geopy.distance import geodesic
import subprocess
import time
import folium
import pandas as pd
import re


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    print(
        """\033[1;94m
             *******************************************************************
             
                  ██████ ██      ███████  █████  ███    ██ ███████ ███████
                 ██      ██      ██      ██   ██ ████   ██ ██      ██
                 ██      ██      █████   ███████ ██ ██  ██ ███████ █████
                 ██      ██      ██      ██   ██ ██  ██ ██      ██ ██
                  ██████ ███████ ███████ ██   ██ ██   ████ ███████ ███████

                        ██ ███    ██     ███    ███  █████  ██████
                           ████   ██     ████  ████ ██   ██ ██   ██
                           ██ ██  ██     ██ ████ ██ ███████ ██████
                           ██  ██ ██     ██  ██  ██ ██   ██ ██
                           ██   ████     ██      ██ ██   ██ ██

             *******************************************************************
        \033[0m"""
    )


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


def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Mapping in {i}...")
        time.sleep(1)


def cleanse_n_map(input_csv_path):
    ssid_list_path = os.path.join(os.path.dirname(__file__), '..', 'utilities', 'ssid_list.txt')
    locations_list_path = os.path.join(os.path.dirname(__file__), '..', 'utilities', 'locations_list.csv')

    with open(ssid_list_path, 'r', errors='ignore') as file:
        ssid_list = [line.strip() for line in file.readlines()]

    locations_list = []
    with open(locations_list_path, 'r', errors='ignore') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                location_name = row[0]
                latitude = float(row[1])
                longitude = float(row[2])
                locations_list.append((location_name, latitude, longitude))
            except ValueError:
                print(f"\033[1;91m Skipping invalid row in locations_list.csv: {row}\033[0m")
            except IndexError as e:
                print(f'\033[1;91m There is an error with the locations list: {e}\033[0m')

    # If you alter the cleansing radius (below) adjust the following message accordingly.
    print(f"\n\033[1;97m A 250m proximity of these {len(locations_list)} locations will be cleansed:\033[0m")
    for location in locations_list:
        print(location)

    cleansed_folder = os.path.join(os.path.dirname(input_csv_path), 'Cleansed4WiGLE')
    os.makedirs(cleansed_folder, exist_ok=True)

    cleansed_csv = os.path.join(cleansed_folder,
                                f"{os.path.splitext(os.path.basename(input_csv_path))[0]}.csv")

    original_row_count = 0
    cleansed_row_count = 0

    try:
        with open(input_csv_path, 'r', errors='ignore') as file:
            cleaned_file = (line.replace('\0', '') for line in file)
            with open(cleansed_csv, 'w', newline='') as output:
                reader = csv.reader(cleaned_file)
                writer = csv.writer(output)

                writer.writerow(next(reader))
                headers = next(reader)
                writer.writerow(headers)

                ssid_idx = headers.index('SSID')
                lat_idx = headers.index('CurrentLatitude')
                lon_idx = headers.index('CurrentLongitude')

                print('\n\033[1;97m Identifying sensitive SSIDs for cleansing...\033[0m')
                rows_to_cleanse = []
                for row in reader:
                    original_row_count += 1
                    if not any(row):
                        break
                    if row[ssid_idx] in ssid_list:
                        rows_to_cleanse.append(row)
                        print(f"\n\033[1;97m Network data identified for cleansing:\033[0m\n{row}")

                file.seek(0)
                cleaned_file = (line.replace('\0', '') for line in file)
                reader = csv.reader(cleaned_file)
                next(reader)
                next(reader)

                print('\n\033[1;97m Checking for proximity to sensitive locations...\033[0m')
                for row in reader:
                    if not any(row):
                        break

                    if len(row) >= 2 and row[ssid_idx] not in ssid_list:
                        row_lat_lon = (float(row[lat_idx]), float(row[lon_idx]))
                        within_proximity_of_location = False

                        if not within_proximity_of_location:
                            for location in locations_list:
                                location_name, location_lat, location_lon = location
                                # edit the following '<=' number according to your needs. Measured in meters.
                                # This specifies the cleansing radius from the specified GPS location.
                                if geodesic(row_lat_lon, (location_lat, location_lon)).meters <= 250:
                                    within_proximity_of_location = True
                                    break

                        if not within_proximity_of_location:
                            writer.writerow(row)
                            cleansed_row_count += 1
                        else:
                            # If you alter the cleansing radius (above) adjust the following message accordingly.
                            if within_proximity_of_location:
                                print(
                                    f" Removing data found within 250m of \033[1;97m{location_name}\033[0m"
                                    f" on row {reader.line_num}")

        def cleansed_stats():
            print(f"\n"
                  f"\033[1;92m Success! Database cleansed...\n"
                  f"\033[1;92m Original records:      {original_row_count}\033[0m")
            print(f"\033[1;92m Remaining records:     {cleansed_row_count}\033[0m")
            difference = original_row_count - cleansed_row_count
            print(f"\033[1;92m Records cleansed:      {difference}\033[0m")
            print(f"\n\033[1;92m Database successfully cleansed of specified SSIDs & locations.\n"
                  f" Saved to:\033[1;97m {cleansed_csv}\n\033[0m")
    except Exception as e:
        print(f'\033[1;91m An error occurred: {e}\033[0m')

    countdown(3)

    try:
        df = pd.read_csv(cleansed_csv, skiprows=1, usecols=['CurrentLatitude', 'CurrentLongitude'],
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

    cleansed_stats()

    print(f"\033[1;92m Success! Map generated...\n"
          f" Cleansed locations in: {initial_count}\n"
          f" Locations sent to map: {final_count}"
          )
    difference = initial_count - final_count
    print(f" Locations dropped:     {difference}\033[0m")

    if points:
        folium.PolyLine(points, color='blue', weight=2.5).add_to(m)

    base_filename = f'Map'
    next_number = get_next_file_number('files/Maps', base_filename)
    map_html_path = os.path.join('files', 'Maps')
    if not os.path.exists(map_html_path):
        os.makedirs(map_html_path)
    map_html_filename = f'{map_html_path}/{base_filename}_{next_number}.html'

    try:
        m.save(map_html_filename)
        print(f'\n\033[1;92m Map saved to\n\033[1;97m {map_html_filename}\n\033[0m')
    except Exception as e:
        print(f"\033[1;91m Error saving map: {e}\033[0m")


clear_console()
banner()
input_csv_path = 'files/DB_files'
input_csv_file = input(
    "\033[1;97m The WiGLE WiFi Wardriving DB file (.csv) must be in the 'files/DB_files' folder.\n"
    "\033[1;93m Enter the input CSV filename (minus '.csv'): \033[0m")
cleanse_n_map(f'{input_csv_path}/{input_csv_file}.csv')

try:
    while True:
        action = input("\n\033[1;93m Press 'enter' to return to the menu:\033[0m").strip().lower()
        if action == '':
            command = f"python3 menu.py"
            subprocess.run(command, shell=True)
            break
except KeyboardInterrupt:
    exit(0)
