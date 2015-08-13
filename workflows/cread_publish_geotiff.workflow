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
.ALGORITHM:script:publishraster
.PARAMETERS:{"UserName": "admin", "StoreName": "landcover_2000", "Password": "geoserver", "DomainName": "192.168.50.169:8080"}
.MODE:Normal
.INSTRUCTIONS:
STEP 3 - Publish the store on geoserver
!INSTRUCTIONS
