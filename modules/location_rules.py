import pandas as pd
import subprocess
import os


def banner():
    print(
        """\033[1;94m
                *******************************************************************

                ██████  ██████  ███████     ██████  ██    ██ ██      ███████ ███████ 
               ██       ██   ██ ██          ██   ██ ██    ██ ██      ██      ██      
               ██   ███ ██████  ███████     ██████  ██    ██ ██      █████   ███████ 
               ██    ██ ██           ██     ██   ██ ██    ██ ██      ██           ██ 
                ██████  ██      ███████     ██   ██  ██████  ███████ ███████ ███████ 
 
                *******************************************************************
        \033[0m"""
    )


file_path = 'utilities/locations_list.csv'


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_data():
    df = pd.read_csv(file_path)
    return df


def save_data(df):
    df = df.sort_values(by='location').reset_index(drop=True)
    df.to_csv(file_path, index=False)


def view_data(df):
    print('\033[1;97m Current locations...\033[0m')
    print(df.to_string(index=True))


def add_location(df):
    try:
        location = input("\033[1;93m Enter the location name: \033[0m")
        print("\033[1;97m Find the location on Google maps, right click on the map and copy the lat/long.\n"
              " Use 'Ctrl+Shift+V' to paste into console and press 'enter'. ")
        lat_long = input("\033[1;93m Enter the latitude and longitude (format: lat, long): \033[0m")
        latitude, longitude = map(str.strip, lat_long.split(", "))
        new_row = pd.DataFrame({
            "location": [location],
            "latitude": [latitude],
            "longitude": [longitude]
        })
        df = pd.concat([df, new_row]).sort_values(by='location').reset_index(drop=True)
        save_data(df)
        clear_console()
        print("\n\033[1;92m Location added successfully, new list...\033[0m")
        return df
    except ValueError:
        print("\033[1;91m Try again...\033[0m")
        return df


def remove_location(df):
    try:
        row_number = int(input("\033[1;93m Enter the row number to delete: \033[0m"))
        if 0 <= row_number < len(df):
            df = df.drop(index=row_number).sort_values(by='location').reset_index(drop=True)
            save_data(df)
            clear_console()
            print("\n\033[1;92m Location removed successfully, new list...\033[0m")
        else:
            print("\033[1;91m Sorry, invalid row number.\033[0m")
    except ValueError:
        print("\033[1;91m Invalid input. Please enter a valid row number.\033[0m\n")
    return df


def rename_location(df):
    try:
        row_number = int(input("\033[1;93m Enter the row number to rename: \033[0m"))
        if 0 <= row_number < len(df):
            new_location = input("\033[1;93m Enter the new location name: \033[0m")
            df.at[row_number, 'location'] = new_location
            df = df.sort_values(by='location').reset_index(drop=True)
            save_data(df)
            clear_console()
            print("\n\033[1;92m Location renamed successfully, new list...\033[0m")
        else:
            print("\033[91m Sorry, invalid row number.\033[0m")
    except ValueError:
        print("\033[1;91m Invalid input. Please enter a valid row number.\033[0m")
    return df


def main():
    df = load_data()

    while True:
        view_data(df)
        print("\n\033[1;97m Use an option below to edit the locations list...")
        print(" \033[1;93ma\033[1;97m       = add location")
        print(" \033[1;93mr\033[1;97m       = rename a location")
        print(" \033[1;93mdelete\033[1;97m  = delete location")
        print("\n or press \033[1;93m'Enter'\033[1;97m to return to the main menu\n\033[0m")
        choice = input("\033[1;93m Choose an option: \033[0m")

        if choice == "a":
            df = add_location(df)
        elif choice == "r":
            df = rename_location(df)
        elif choice == "delete":
            df = remove_location(df)
        elif choice == "":
            try:
                clear_console()
                command = f"python3 menu.py"
                subprocess.run(command, shell=True)
                break
            except KeyboardInterrupt:
                exit(0)
        else:
            print("\033[1;91m Invalid choice, try again...\033[0m")


banner()
main()
