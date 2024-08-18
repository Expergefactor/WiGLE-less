# WiGLE-less
WiGLE Wardriving...just a little bit less. 
    
### WHAT IS IT?
This software is designed to be used with CSV files exported from the WiGLE WiFi
Wardriving app (DATABASE>CSV EXPORT DB - Export entire DB to CSV file). The software
can remove records of specified networks (SSIDs) and records within a proximity of
specified (GPS) locations whilst retaining the file format and metadata to allow
remaining data to contribute to the WiGLE project (if desired).

Default proximities set at:
* 150m of a set SSID
* 250m of a set location

Proximity values can be edited in the code. A note has been added to areas which can be etited for location proximities only but SSID proximity can also be edited if you find the right parts to edit. 

### WHY?
WiGLE-less is a toolkit for people wanting to:

* Contribute to the WiGLE project in a (slightly) anonymous manner,
* Have the ability to remove specified Wi-Fi networks from a database export prior to uploading to the WiGLE project,
* Have the ability to remove specified locations from a database export prior to uploading to the WiGLE project,
* Build incremental, 'Wardriven' maps from the cleansed data to display routes within the processed data,
* Combine previously generated 'Wardriven' maps into a single 'Master' map, without wanting to retain copies of the database files other than for the purposes above.

### SERIOUSLY, WHAT'S THE POINT?
It has purpose for me. If you can think of one too, great!
If nothing else, it's a convoluted method of mapping your travels :)

While you're here, I'm no developer. This is a hobby built from scratch. I'm sure that
the code is, errm..., please be kind or constructive :) 
  
### DEVELOPED WITH:
 WiGLE WiFi Wardriving app      - Version v.2.85 for Android
 Wardrive device                - Android 7.0
 PyCharm                        - https://www.jetbrains.com/pycharm/
 OnlyOffice Desktop Editors     - https://www.onlyoffice.com/download-desktop.aspx

DB saved to local storage (Android) using a File Browser & extracted with Gnome.

### TESTED WITH:
* Max. DB size circa. 400k records
* Over 20 specified locations
* Under 10 specified networks
  
Processing time varies with size of DB to be processed (& obviously your hardware).

### REQUIREMENTS:
* Python
* geopy (built with version 2.4.1)
* pandas (built with version 2.2.2)
* matplotlib (built with version 3.9.1)
* folium (built with version 0.17.0)

Use: 

    pip install geopy pandas matplotlib folium

### What do I do?
* Download the repo as a zip and unpack to a local directory.
* Run:

        python3 menu.py

### SUMMARY OF FUNCTIONS...
 1  Cleanse WiGLE DB dump & generate a cleansed Wardriven map (CSV > CSV & HTML)
     This cleanses a WiGLE Wardriving database export (CSV) and removes records
     containing specified SSIDs (function 3) & specified locations (function 4).
     Put a copy of the original DB file in the 'files/DB_files' folder. Cleansed
     DB files are generated in a subfolder created, 'files/DB_files/Cleansed4WiGLE'.
     The cleansed database is then used to build a map that displays routes 'Wardriven'
     from the remaining data. The map generated is a HTML based OpenStreetMap overlaid
     with the routes.

 2  Merge all cleansed maps generated with function 1 (HTML > HTML)
     To merge maps, they must be in the original format, output folder and (at least)
     be named 'Map_'. Original files will remain untouched and a new map will be generated.

 3  View, add or remove SSIDs as cleansing rules
     This is a list of SSIDs that will be removed from a WiGLE WiFi Wardriving database
     CSV dump when using function 1. The SSID should be input exactly as would be seen
     on-screen if you were to try and join the network.

 4  View, add or remove locations as cleansing cleansing rules
     Add or remove locations that will be removed from a WiGLE WiFi Wardriving database
     CSV dump when using function 1. Locations are set to a 500m radius of a set GPS location.
     Instructions are provided when using the function.

 5  Manually create/recreate a Wardriven map (CSV > HTML)
     Want to map an original, un-cleansed CSV database? Regenerate a cleansed map?
     Use this function. The CSV file used to generate the map must be within the 
     'files/DB_files' directory.

 6 Erase original database files
     Optimised for full disk encrypted SSDs, this performs a single pass overwrite on all
     files in the 'files/DB_files' directory before deleting them. This aims to balance
      secure data erasure while prolonging SSD lifespan. Does not touch cleansed files.
     NOTE: This is not a method of securely destroying data on a traditional HDD.

 7 Erase cleansed database files
     As per function 6 but for the cleansed database files produced by function 1
     i.e. all files in the 'files/DB_files/Cleansed4WiGLE' directory.

### IN SUPPORT OF:
  WiGLE - https://wigle.net Thanks to bobzilla & the team, keep up the amazing work!
  
  Upload database files here: https://wigle.net/uploads/
