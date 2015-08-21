import requests
import json

# The data entry form
##Geoserver_URL=string http://host[:port]/geoserver
# test -> ##Geoserver_URL=string http://192.168.50.171:8080/geoserver
##Username=string your_username
##Password=string your_password
##Image_mosaic_Store_Name=string a datastore name
# ##Image_mosaic_Store_Name=string countryMosaic
##Mosaic_Granule_to_add=vector

usr=Username
pswd=Password
geoserver_url=Geoserver_URL
store_name=Image_mosaic_Store_Name
granule_abs_path=Mosaic_Granule_to_add
base_rest_path="/rest/imports"

print "STEP 1 - Creating a new importer for the datastore: '" + store_name + "'..."
headers = {'content-type': 'application/json'}
jsonRunImporter = '{"import": {"targetWorkspace": {"workspace": {"name": "geonode"}},"targetStore": {"dataStore": {"name": "' + str(store_name) + '"}}}}'
print(jsonRunImporter)
url = geoserver_url + base_rest_path
r = requests.post(url, jsonRunImporter, auth=(usr, pswd), headers=headers)
print(r.text)
data = json.loads(r.text)
importerId = data["import"]["id"]
print "...importer successfuly created! importerId:'" + str(importerId) + "'"

print ""

print "STEP 2 - Going to load from filesystem the geotif to upload..."
upload = {'files': ('country.tiff', open(granule_abs_path, "rb"), 'application/octet-stream')}
print "...geotif successfuly loaded! ready to create a run a task for the importer " + str(importerId) + "..."
url  += "/" + str(importerId) + "/tasks" 
r = requests.post(url, files=upload, auth=(usr, pswd))
print "...task created! taskId: '" + ""

print ""

data = json.loads(r.text)
taskId = data["task"]["id"]
print "STEP 3 - Importer: '" + str(importerId) +"' run taskId: '" + str(taskId) + "'"
url  = url = geoserver_url + base_rest_path + "/" + str(importerId)
print str(url)
r = requests.post(url, auth=(usr, pswd))
print "task started!"







