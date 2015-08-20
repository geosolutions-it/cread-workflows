.NAME:Process and Publish CSV
.GROUP:C-READ
.ALGORITHM:script:createvrt
.PARAMETERS:{"Geometry_encoding": "wkt", "Geometry_type": "wkbPoint", "Layer_name": "a_layer_name", "Geometry_field_name": "the_geom"}
.MODE:Normal
.INSTRUCTIONS:
GEONODE CSV PUBLISHER

-WORKFLOW Overview-
Geospatial vector data exported from 3rd party systems are often in CSV format.

CSV format is not directly supported in many GIS software so often the CSV datasource is converted into a ESRI Shapefile (Steps 1, 2)

Having a shapefile data extraction with
SQL is performed (Step 3)

The layer will be at the end published on a Geonode istance (Step 4)

STEP 1/4 - VRT Creation

In order to be able to do convert a CSV in a Shapefile an intermediate format called  VRT (ViRtual Format) file must be provided.
More information about mapping a CSV on a VRT are here: http://www.gdal.org/gdal_vrttut.html

MAIN PARAMS 

Layer name -> the name of the csv file without the extension ".csv"

src Datasource -> the input CSV file

NOTE: Layer name must be the same of the src Datasource

!INSTRUCTIONS
.ALGORITHM:gdalogr:convertformat
.PARAMETERS:{"OPTIONS": "", "FORMAT": 0}
.MODE:Normal
.INSTRUCTIONS:

STEP 2/4 - Conversion from CSV to SHP

This step translate a CSV layer in a shapefile layer and import it into QGIS.

The conversion will be then performed using ogr2ogr command from the GDAL's OGR utilities. http://www.gdal.org/ogr2ogr.html

MAIN PARAMS

Input Vector: the VRT created in the previous step using the input CSV
!INSTRUCTIONS
.ALGORITHM:gdalogr:executesql
.PARAMETERS:{"SQL": "select * from OUTPUTLAYER where [attribute]='[value]'"}
.MODE:Normal
.INSTRUCTIONS:
STEP 3/4 - Data extraction

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
STEP 4/4 - Geonode Layer publication

Publish the Shapefile layer created on a Geonode instance

MAIN PARAMS

Geonode URL
The base URL of the Geonode instance.
examples:
http://192.168.50.170:8000
http://awebsite.geonode.org

User
A Username who has the publications grants required

Password
The user password

Vector Layer
The previously created layer opened in the current project

Title 
A geonode metyadata

Abstact
A geonode metyadata
!INSTRUCTIONS
