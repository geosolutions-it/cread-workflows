import os
from cread.geonodemanager import GeonodeManager

# ##DomainName=string host[:port]
##DomainName=string 192.168.50.170:8080
# ##StoreName=string landcover_2000
##StoreName=string landcover_2000
# ##Filename=string insert the absolute path of a mosaic granule here
##Layer=raster
##UserName=string admin
##Password=string geoserver

myfilepath = processing.getObject(Layer).dataProvider().dataSourceUri()
(myDirectory,nameFile) = os.path.split(myfilepath)

file_abs_path = myDirectory + '/' + nameFile

GeonodeManager(str(UserName), str(Password), str(DomainName)).publish_coveragestore(str(file_abs_path), str(StoreName))