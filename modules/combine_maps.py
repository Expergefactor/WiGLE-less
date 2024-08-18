import os
import glob
from bs4 import BeautifulSoup
import folium
from datetime import datetime
import re
import subprocess


def banner():
    print("""\033[1;94m
              *******************************************************************
    
     ███    ███ ███████ ██████   ██████  ███████     ███    ███  █████  ██████  ███████
     ████  ████ ██      ██   ██ ██       ██          ████  ████ ██   ██ ██   ██ ██
     ██ ████ ██ █████   ██████  ██   ███ █████       ██ ████ ██ ███████ ██████  ███████
     ██  ██  ██ ██      ██   ██ ██    ██ ██          ██  ██  ██ ██   ██ ██           ██
     ██      ██ ███████ ██   ██  ██████  ███████     ██      ██ ██   ██ ██      ███████
    
              *******************************************************************
          \033[0m"""
          )


def merge_maps():
    print("\033[1;97m All maps (Map_*.html) in the 'files/Maps' directory will be merged...\033[0m ")
    input_directory = 'files/Maps/'
    output_directory = 'files/Maps/'

    map_files = glob.glob(os.path.join(input_directory, 'Map_*.html'))

    if not map_files:
        print("\033[1;91m Sorry, no maps to merge in the 'files/Maps' directory.\033[0m")
        return

    master_map = folium.Map(location=[52.923441783344245, -1.4717772277682117], zoom_start=7)

    for map_file in map_files:
        try:
            with open(map_file, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')
                script_tags = soup.find_all('script')

                for script in script_tags:
                    if 'L.polyline' in script.text:
                        coordinates_str = re.findall(r'\[\[.*?\]\]', script.text)
                        for coord_str in coordinates_str:
                            try:
                                coordinates = eval(coord_str)
                                folium.PolyLine(coordinates, color='blue', weight=2.5).add_to(master_map)
                            except SyntaxError as e:
                                print(f"\033[1;91m Failed to parse coordinates in file {map_file}: {e}\033[0m")
        except Exception as e:
            print(f"\033[1;91m Failed to process file {map_file}: {e}\033[om")

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"Master_Map_{current_time}.html"
    output_path = os.path.join(output_directory, output_filename)

    master_map.save(output_path)
    print(f"\033[1;92m Success!\n Master map saved: \033[1;97m{output_path}\033[0m")


banner()
merge_maps()
try:
    while True:
        action = input("\n\033[1;93m Press 'Enter' to return to the menu: \033[0m").strip().lower()
        if action == '':
            command = f"python3 menu.py"
            subprocess.run(command, shell=True)
            break
except KeyboardInterrupt:
    exit(0)
