# WiGLE-less
WiGLE Wardriving...just a little bit less. 
    
### WHAT IS IT?
This software is designed to be used with CSV files exported from the WiGLE WiFi
Wardriving app (DATABASE>CSV EXPORT DB - Export entire DB to CSV file). The software
can remove records of specified networks (SSIDs) and records within a proximity of
specified (GPS) locations whilst retaining the file format and metadata to allow
remaining data to contribute to the WiGLE project (if desired).

### WHY?
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
    Max. DB size circa. 400k records
    >20 specified locations
    <10 specified networks
Processing time varies with size of DB to be processed (& obviously your hardware).

### REQUIREMENTS:
  * Python
  * geopy (built with version 2.4.1)
  * pandas (built with version 2.2.2)
  * matplotlib (built with version 3.9.1)
  * folium (built with version 0.17.0)
Use: 
      $ pip install geopy pandas matplotlib folium

### IN SUPPORT OF:
  WiGLE - https://wigle.net/
      
  Thanks to bobzilla & the team, keep up the amazing work!
  Upload database files here: https://wigle.net/uploads/
