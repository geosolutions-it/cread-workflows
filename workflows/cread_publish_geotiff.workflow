.NAME:Process and Publish Geotif
.GROUP:C-READ
.ALGORITHM:gdalogr:translate
.PARAMETERS:{"ZLEVEL": 6, "SDS": false, "OUTSIZE": 100, "OUTSIZE_PERC": true, "RTYPE": 5, "COMPRESS": 4, "NO_DATA": "", "BIGTIFF": 0, "TILED": false, "JPEGCOMPRESSION": 75, "TFW": false, "PREDICTOR": 1, "EXPAND": 0, "EXTRA": ""}
.MODE:Normal
.INSTRUCTIONS:
STEP 1 - Perform retiling

http://www.gdal.org/gdal_translate.html
!INSTRUCTIONS
.ALGORITHM:gdalogr:overviews
.PARAMETERS:{"LEVELS": "2 4 8 16", "RESAMPLING_METHOD": 0, "CLEAN": false, "FORMAT": 0}
.MODE:Normal
.INSTRUCTIONS:
STEP 2 - Create the embedded Overviews

http://www.gdal.org/gdal_translate.html
!INSTRUCTIONS
.ALGORITHM:script:geonoderasterpublisher
.PARAMETERS:{"Abstract": "Insert a description", "Password": "your_password", "User": "admin", "Geonode_URL": "http://192.168.50.170:8000", "Title": "Insert a tiltle"}
.MODE:Normal
.INSTRUCTIONS:
!INSTRUCTIONS
