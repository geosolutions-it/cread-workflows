from geonodemanager import GeonodeManager

##DomainName=string 192.168.50.169:8080
##StoreName=string belize_roads_coverage_1
##Filename=string D:\\work\\data\\c-read\\belize_roads_coverage_1.zip
##UserName=string admin
##Password=string geoserver

GeonodeManager("admin", "geoserver", "192.168.50.169:8080").publish_datastore("D:\\work\\data\\c-read\\population_estimates_2010_2013.zip", "population_estimates_2010_2013")