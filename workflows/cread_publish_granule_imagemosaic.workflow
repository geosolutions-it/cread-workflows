.NAME:Process and Publish Image Mosaic Granule
.GROUP:C-READ
.ALGORITHM:gdalogr:translate
.PARAMETERS:{"ZLEVEL": 6, "SDS": false, "OUTSIZE": 100, "OUTSIZE_PERC": true, "RTYPE": 5, "COMPRESS": 4, "NO_DATA": "", "BIGTIFF": 0, "TILED": false, "JPEGCOMPRESSION": 75, "TFW": false, "PREDICTOR": 1, "EXPAND": 0, "EXTRA": ""}
.MODE:Normal
.INSTRUCTIONS:
!INSTRUCTIONS
.ALGORITHM:gdalogr:overviews
.PARAMETERS:{"LEVELS": "2 4 8 16", "RESAMPLING_METHOD": 0, "CLEAN": false, "FORMAT": 0}
.MODE:Normal
.INSTRUCTIONS:
!INSTRUCTIONS
.ALGORITHM:script:publishmosaicgranule
.PARAMETERS:{"Geoserver_URL": "http://192.168.50.170:8080/geoserver", "Image_mosaic_Store_Name": "countryMosaic"}
.MODE:Normal
.INSTRUCTIONS:
!INSTRUCTIONS
