.NAME:Process and Publish CSV
.GROUP:C-READ
.ALGORITHM:script:createvrt
.PARAMETERS:{"Geometry_encoding": "wkt", "Geometry_type": "wkbPoint", "Layer_name": "a_layer_name", "Geometry_field_name": "the_geom"}
.MODE:Normal
.INSTRUCTIONS:
!INSTRUCTIONS
.ALGORITHM:gdalogr:convertformat
.PARAMETERS:{"OPTIONS": "", "FORMAT": 0}
.MODE:Normal
.INSTRUCTIONS:

STEP 1 - Conversion from CSV to SHP

-Overview-
Geospatial vector data exported from 3rd party systems are often in CSV format.

CSV format is not directly supported in many GIS software and usually some configuration steps are needed in order to work with it.

This step translate a CSV layer in a shapefile layer and import it into QGIS.

In order to be able to do this conversion a VRT (ViRtual Format) file must be provided.
More information about mapping a CSV on a VRT are here: http://www.gdal.org/gdal_vrttut.html

The conversion will be then performed using ogr2ogr command from the GDAL's OGR utilities. http://www.gdal.org/ogr2ogr.html
!INSTRUCTIONS
.ALGORITHM:gdalogr:executesql
.PARAMETERS:{"SQL": "select * from OUTPUTLAYER where [attribute]='[value]'"}
.MODE:Normal
.INSTRUCTIONS:
STEP 2 - Data extraction

From the dataset created in the previous step can we can extract a subset of features.

The sql query as the second parameter in this form will be performed on the layer selected in the above dropdown list, no matter if the layer is stored on a non DBMS datasource.

Substitute [attribute] with the name of the feature attribute you want to filter on and [value] with the value of that attribute.

You can also improve that query performing a more complex filtering but be aware of:

-> "select * from OUTPUTLAYER" is fixed, you can change only the where clausule

-> DON'T delete the quote around the [attribute] when you replace the value!
!INSTRUCTIONS
.ALGORITHM:script:geonodevectorpublisher
.PARAMETERS:{"Abstract": "Insert a description", "Password": "your_password", "User": "admin", "Geonode_URL": "http://192.168.50.170:8000", "Title": "Insert a tiltle"}
.MODE:Normal
.INSTRUCTIONS:
!INSTRUCTIONS
