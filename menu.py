import subprocess
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    print(
        """\033[1;94m
            *******************************************************************
            
        ██     ██ ██  ██████  ██      ███████       ██      ███████ ███████ ███████ 
        ██     ██    ██       ██      ██            ██      ██      ██      ██      
        ██  █  ██ ██ ██   ███ ██      █████   █████ ██      █████   ███████ ███████ 
        ██ ███ ██ ██ ██    ██ ██      ██            ██      ██           ██      ██ 
         ███ ███  ██  ██████  ███████ ███████       ███████ ███████ ███████ ███████ 
                                        \033[1;92mby Expergefactor\033[1;94m
                                            v.1.0
                                          
            *******************************************************************
        \033[0m"""
    )


def about():
    print("""\033[1;97m
    WiGLE-less \033[1;92mby Expergefactor...
    \033[1;93m
    WHAT IS IT?\033[1;97m
    This software is designed to be used with CSV files exported from the WiGLE WiFi
    Wardriving app (DATABASE>CSV EXPORT DB - Export entire DB to CSV file). The software
    can remove records of specified networks (SSIDs) and records within a proximity of
    specified (GPS) locations whilst retaining the file format and metadata to allow
    remaining data to contribute to the WiGLE project (if desired).
    \033[1;93m
    WHY?\033[1;97m
    WiGLE-less is a toolkit for people wanting to:
        * Contribute to the WiGLE project in a (slightly) anonymous manner,
        * Have the ability to remove specified Wi-Fi networks from a database export
          prior to uploading to the WiGLE project,
        * Have the ability to remove specified locations from a database export
          prior to uploading to the WiGLE project,
        * Build incremental, 'Wardriven' maps from the cleansed data to display routes
          within the processed data,
        * Combine previously generated 'Wardriven' maps into a single 'Master' map,
    without wanting to retain copies of the database files other than for the purposes above.
    \033[1;93m
    SERIOUSLY, WHAT'S THE POINT?\033[1;97m
        It has purpose for me. If you can think of one too, great!
        If nothing else, it's a convoluted method of mapping your travels :)

        While you're here, I'm no developer. This is a hobby built from scratch. I'm sure that
        the code is, errm..., please be kind or constructive :) 
    \033[1;93m  
    DEVELOPED WITH:\033[1;97m
     WiGLE WiFi Wardriving app      - Version v.2.85 for Android
     Wardrive device                - Android 7.0
     PyCharm                        - https://www.jetbrains.com/pycharm/
     OnlyOffice Desktop Editors     - https://www.onlyoffice.com/download-desktop.aspx
    
    DB saved to local storage (Android) using a File Browser & extracted with Gnome.
    \033[1;93m
    TESTED WITH:\033[1;97m
        Max. DB size circa. 400k records
        >20 specified locations
        <10 specified networks
    Processing time varies with size of DB to be processed (& obviously your hardware).
    \033[1;93m
    REQUIREMENTS:\033[1;97m
        * Python
        * geopy (built with version 2.4.1)
        * pandas (built with version 2.2.2)
        * matplotlib (built with version 3.9.1)
        * folium (built with version 0.17.0)
    Use: 
        $ pip install geopy pandas matplotlib folium
    \033[1;93m
    IN SUPPORT OF:\033[1;97m
        WiGLE - https://wigle.net/
        
    Thanks to bobzilla & the team, keep up the amazing work!
    Upload database files here: https://wigle.net/uploads/
    \033[1;91m
    *******************************************************************************
                                    LICENCE
                WiGLE-less by Expergefactor Copyright (c) 2024.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    *******************************************************************************
    \033[0m
    """)
    input("\033[1;93m Press 'enter' key to continue: \033[0m")
    main()


def choices():
    try:
        while True:
            search_type_choice = input(
                " \033[1;97m What would you like to do?\n\n\033[0m"
                " \033[1;93m1\033[1;97m Cleanse WiGLE DB dump & generate a cleansed Wardriven map\n"
                " \033[1;93m2\033[1;97m Merge all cleansed maps generated with function 1.\n"
                " \033[1;93m3\033[1;97m View, add or remove SSIDs as cleansing rules\n"
                " \033[1;93m4\033[1;97m View, add or remove locations as cleansing cleansing rules\n"
                " \033[1;93m5\033[1;97m Manually create/recreate a Wardriven map\n"
                " \033[1;93m6\033[1;97m Erase the Original Database Files\n"
                " \033[1;93m7\033[1;97m Erase the Cleansed Database Files\n"
                " \033[1;93ms\033[1;97m Summary of functions\n"
                " \033[1;93ma\033[1;97m About\n"
                " \033[1;93me\033[1;97m Exit\n\n\033[0m"
                " \033[1;93mInput a value and press 'enter': \033[0m"
            )
            if search_type_choice == "1":
                command = f"python3 modules/cleanse_n_mapit.py"
                clear_console()
                subprocess.run(command, shell=True)
                break
            if search_type_choice == "2":
                command = f"python3 modules/combine_maps.py"
                clear_console()
                subprocess.run(command, shell=True)
                break
            if search_type_choice == "3":
                command = f"python3 modules/ssid_rules.py"
                clear_console()
                subprocess.run(command, shell=True)
                break
            if search_type_choice == "4":
                command = f"python3 modules/location_rules.py"
                clear_console()
                subprocess.run(command, shell=True)
                break
            if search_type_choice == "5":
                command = f"python3 modules/mapit.py"
                clear_console()
                subprocess.run(command, shell=True)
                break
            if search_type_choice == "6":
                command = f"python3 modules/erase_original_db.py"
                clear_console()
                subprocess.run(command, shell=True)
                break
            if search_type_choice == "7":
                command = f"python3 modules/erase_cleansed_db.py"
                clear_console()
                subprocess.run(command, shell=True)
                break
            if search_type_choice == "s":
                print("\n\033[1;97m"
                      " For information about this software, use the 'a' (About) function.\n\n"
                      " \033[1;93mSUMMARY OF FUNCTIONS...\n"
                      " \033[1;93m1\033[1;97m  Cleanse WiGLE DB dump & generate a cleansed Wardriven map"
                      " (CSV > CSV & HTML)\033[0m\n"
                      "     This cleanses a WiGLE Wardriving database export (CSV) and removes records\n"
                      "     containing specified SSIDs (function 3) & specified locations (function 4).\n"
                      "     Put a copy of the original DB file in the 'files/DB_files' folder. Cleansed\n"
                      "     DB files are generated in a subfolder created, 'files/DB_files/Cleansed4WiGLE'.\n"
                      "     The cleansed database is then used to build a map that displays routes 'Wardriven'\n"
                      "     from the remaining data. The map generated is a HTML based OpenStreetMap overlaid\n"
                      "     with the routes.\n\n"
                      " \033[1;93m2\033[1;97m  Merge all cleansed maps generated with function 1 (HTML > HTML)\n\033[0m"
                      "     To merge maps, they must be in the original format, output folder and (at least)\n"
                      "     be named 'Map_'. Original files will remain untouched and a new map will be generated.\n\n"
                      " \033[1;93m3\033[1;97m  View, add or remove SSIDs as cleansing rules\n\033[0m"
                      "     This is a list of SSIDs that will be removed from a WiGLE WiFi Wardriving database\n"
                      "     CSV dump when using function 1. The SSID should be input exactly as would be seen\n"
                      "     on-screen if you were to try and join the network.\n\n"
                      " \033[1;93m4\033[1;97m  View, add or remove locations as cleansing cleansing rules\n\033[0m"
                      "     Add or remove locations that will be removed from a WiGLE WiFi Wardriving database\n\033[0m"
                      "     CSV dump when using function 1. Locations are set to a 500m radius of a set GPS location.\n"
                      "     Instructions are provided when using the function.\n\n"
                      " \033[1;93m5\033[1;97m  Manually create/recreate a Wardriven map (CSV > HTML)\n\033[0m"
                      "     Want to map an original, un-cleansed CSV database? Regenerate a cleansed map?\n"
                      "     Use this function. The CSV file used to generate the map must be within the \n"
                      "     'files/DB_files' directory.\n\n"
                      " \033[1;93m6\033[1;97m Erase original database files\n\033[0m"
                      "     Optimised for full disk encrypted SSDs, this performs a single pass overwrite on all\n"
                      "     files in the 'files/DB_files' directory before deleting them. This aims to balance\n "
                      "     secure data erasure while prolonging SSD lifespan. Does not touch cleansed files.\n"
                      "     NOTE: This is not a method of securely destroying data on a traditional HDD.\n\n"
                      " \033[1;93m7\033[1;97m Erase cleansed database files\n\033[0m"
                      "     As per function 6 but for the cleansed database files produced by function 1\n"
                      "     i.e. all files in the 'files/DB_files/Cleansed4WiGLE' directory.\n\n"
                      " \033[1;93ms\033[1;97m  Display this message.\n\n\033[0m"
                      " \033[1;93ma\033[1;97m  Display the 'About' page.\033[0m\n"
                      "     Contains details of the software build, purpose & licence.\n\n")
                input("\033[1;93m Press 'Enter' key to continue\033[0m")
                main()
            if search_type_choice == "e":
                print("\n\033[1;92m Program terminated by user...\033[0m\n")
                exit(0)
            if search_type_choice == "a":
                about()
            else:
                print("\n\033[1;91m Invalid option, try again...\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[1;92m Exiting...\033[0m\n")
        exit(0)
    except Exception as e:
        print(f' Error: {e}')


def main():
    clear_console()
    banner()
    choices()


main()
