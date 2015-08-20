.NAME:Process and Publish Image Mosaic Granule
.GROUP:C-READ
.ALGORITHM:gdalogr:translate
.PARAMETERS:{"ZLEVEL": 6, "SDS": false, "OUTSIZE": 100, "OUTSIZE_PERC": true, "RTYPE": 5, "COMPRESS": 4, "NO_DATA": "", "BIGTIFF": 0, "TILED": false, "JPEGCOMPRESSION": 75, "TFW": false, "PREDICTOR": 1, "EXPAND": 0, "EXTRA": ""}
.MODE:Normal
.INSTRUCTIONS:
OPTIMIZE and PUBLISH RASTER LAYER

-WORKFLOW OVERVIEW-
Any raster published on a geospatial server must be optimized in order to be efficently served to the clients

This workflow compute the raster retiling and creates its overviews using GDAL-Translate for the former and GDAL-addo for the latter action (Steps 1, 2)

The optimized layer will be at the end (Step 3) published on Geonode as a single-image Raster Layer

STEP 1/3 - Perform retiling

Uses GDAL-Translate to perform retiling and improve pan actions on the layer once published

See the GDAL documentation http://www.gdal.org/gdal_translate.html

MAIN PARAMS

Input Vector
Select on the file system the raster to process
!INSTRUCTIONS
.ALGORITHM:gdalogr:overviews
.PARAMETERS:{"LEVELS": "2 4 8 16", "RESAMPLING_METHOD": 0, "CLEAN": false, "FORMAT": 0}
.MODE:Normal
.INSTRUCTIONS:
STEP 2/3 - Create the embedded Overviews

Uses GDAL-Addo to create overviews to improve zoom actions of the layer

See the GDAL documentation http://www.gdal.org/gdal_translate.html

MAIN PARAMS

Input Vector
Select on the file system the raster to process
!INSTRUCTIONS
.ALGORITHM:script:publishmosaicgranule
.PARAMETERS:{"Geoserver_URL": "http://192.168.50.170:8080/geoserver", "Image_mosaic_Store_Name": "countryMosaic"}
.MODE:Normal
.INSTRUCTIONS:
STEP 4/4 - Geoserver ImageMosaic update

Update an Image mosaic with the raster layer created.

The raster will be directly published on  Geoserver , adding a one more time instance to an Imagemosaic datastore

MAIN PARAMS

Geoserver URL
The base URL of the Geonode instance.
examples:
http://192.168.50.170:8080/geosever
http://awebsite.geonode.org/geoserver

Image mosaic Store Name
The name of the datastore published on Geoserver

Image mosaic Granule to add
The previously created layer opened in the current project
!INSTRUCTIONS
