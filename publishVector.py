from cread.geonodemanager import GeonodeManager
import os
import zipfile

# The data entry form
##DomainName=string host[:port]
##StoreName=string police_station_wgs84
##Layer=vector
##UserName=string admin
##Password=string geoserver

# Get the path on FileSystem of the layer loaded on QGIS and selected by the user
myfilepath = processing.getObject(Layer).dataProvider().dataSourceUri()

# Access to the shapefile folder and create a zip to upload it using geoserver REST interface
(myDirectory,nameFile) = os.path.split(myfilepath)
zipf = zipfile.ZipFile(os.path.join(myDirectory,'shpUpload.zip'), 'w')
for file in os.listdir(myDirectory):
    print file
    if(str(file) != "shpUpload.zip"):
        print myDirectory
        print os.path.join(myDirectory, str(file))
        print os.path.relpath(os.path.join(myDirectory, str(file)), myDirectory)
        zipf.write(os.path.join(myDirectory, str(file)), str(file))
zipf.close()
zip = str(os.path.join(myDirectory, 'shpUpload.zip'))

# Publish a datastore (e.g. a vector layer)
GeonodeManager(UserName, Password, str(DomainName)).publish_datastore(zip, str(StoreName))