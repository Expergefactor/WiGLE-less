import os
import subprocess


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    print(
        """\033[1;94m
                *******************************************************************

              ███████ ███████ ██ ██████      ██████  ██    ██ ██      ███████ ███████
              ██      ██      ██ ██   ██     ██   ██ ██    ██ ██      ██      ██
              ███████ ███████ ██ ██   ██     ██████  ██    ██ ██      █████   ███████
                   ██      ██ ██ ██   ██     ██   ██ ██    ██ ██      ██           ██
              ███████ ███████ ██ ██████      ██   ██  ██████  ███████ ███████ ███████

                *******************************************************************
        \033[0m"""
    )


def cleansing_rules():
    try:
        clear_console()
        banner()
        file_path = 'utilities/ssid_list.txt'

        # Check if the file exists and read the SSIDs into a set
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                ignore_ssids = set(line.strip() for line in file)
        else:
            ignore_ssids = set()

        print("\033[1;97m SSIDs for cleansing: \033[0m\n")
        for ssid in ignore_ssids:
            print(ssid)

        while True:
            print("\n\033[1;97m Use an option below to edit the SSIDs list...\n")
            print(" \033[1;93ma\033[1;97m       = add location")
            print(" \033[1;93mdelete\033[1;97m  = delete location")
            print("\n or press \033[1;93m'enter'\033[1;97m to return to the menu...\033[0m")
            action = input("\033[1;93m Choose an option: \033[0m")

            if action == 'a':
                new_ssids = input("\033[1;93m Enter the SSID: \033[0m").strip().split(',')
                ignore_ssids.update(ssid.strip() for ssid in new_ssids)
                with open(file_path, 'w') as file:
                    for ssid in ignore_ssids:
                        file.write(ssid + '\n')
                clear_console()
                print("\033[1;92m\n SSID added. SSIDs to be cleansed...\033[0m\n")
                for ssid in ignore_ssids:
                    print(ssid)

            elif action == 'delete':
                ssids_to_remove = input("\033[1;93m Enter SSID(s) to delete: \033[0m").strip().split(',')
                ignore_ssids.difference_update(ssid.strip() for ssid in ssids_to_remove)
                with open(file_path, 'w') as file:
                    for ssid in ignore_ssids:
                        file.write(ssid + '\n')
                clear_console()
                print("\033[1;92m\n SSID deleted. SSIDs to be cleansed...\033[0m\n")
                for ssid in ignore_ssids:
                    print(ssid)
                return cleansing_rules()

            elif action == '':
                command = f"python3 menu.py"
                subprocess.run(command, shell=True)
                break

            else:
                print("\033[1;91m\n Invalid choice, try again...\033[0m")

    except KeyboardInterrupt:
        exit(0)


cleansing_rules()
