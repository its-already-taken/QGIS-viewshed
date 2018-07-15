# QGIS-viewshed
scripts that enable viewshed analyses in QGIS using CLI

Developed for RADAR and Multilateration (MLAT) coverage analyses.

SETUP:
1. Install QGIS 2.18 LTR in default location (C:\Program Files\QGIS 2.18\)
2. Create folder C:\QGIS\
3. Create folders C:\QGIS\dane\ and C:\QGIS\temp\
4. Copy all git-listed files to C:\QGIS\skrypty\
5. Edit lokalizacje.txt
   each line of the file contains a location description, eg.
     1,Zabierzow,50.10916667,19.77944444,40,300
     3 Zab       49.3425     19.9675     10 300
   stands for: layer number, location name, LAT, LON, antenna height [mAGL], target height [mAGL],
   note that variables may be separated by comma (CSV format) or by any number of spaces.
6. From data of choice - eg. SRTM, prepare a digital elevation model (DEM) of the terrain of interest,
   save your model to a NMT.gif (GTiff format) and place it in C:\QGIS\dane\
   In LOS.py edit the line marked "# zasieg - ..." with a LAT/LON frame suitable for your region of analysis, eg.
     "14.11666667,24.13333333,49.000000,54.83333333"
   stands for the furthest points of Poland.
7. Run uruchom.bat
8. A time-stamped output directory will be created in C:\QGIS\
   *.shp files may be displayed or further processed in QGIS,
   they contain the viewshed analisys for each location (line of the lokalizacje.txt file),
   use a background layer of choice to plot the viewshed against terrain.
