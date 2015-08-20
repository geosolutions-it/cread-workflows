import requests
import json
import os
import zipfile

# ##############################
# GUI: The data entry form
#
# ##Geonode_URL=string http://host[:port]
#
##Geonode_URL=string http://192.168.50.170:8000
##User=string admin
##Password=string your_password
##Raster_Layer=raster
##Title=string Insert a tiltle
##Abstract=string Insert a description


# #############################
# Private Functions
#
# Access to the shapefile folder and create a zip to upload it using geoserver REST interface
#

# Creates a zip archive of the layer (shp) selected in the current qgis project 
def zipLayer (myfilepath):
    (myDirectory,nameFile) = os.path.split(myfilepath)
    zipf = zipfile.ZipFile(os.path.join(myDirectory,'shpUpload.zip'), 'w')
    for file in os.listdir(myDirectory):
        print file
        if(str(file) != "shpUpload.zip"):
            print 'myDirectory' + myDirectory
            print 'dir+file' + os.path.join(myDirectory, str(file))
            print 'relativepath' + os.path.relpath(os.path.join(myDirectory, str(file)), myDirectory)
            zipf.write(os.path.join(myDirectory, str(file)), str(file))
    zipf.close()
    zip = str(os.path.join(myDirectory, 'shpUpload.zip'))
    return zip


user=User
password=Password

layer_data = Raster_Layer
data_type='raster'

login_path='/account/login/?next=/'
upload_path='/layers/upload'

layer_title=Title
abstract=Abstract

base_url = Geonode_URL
login_url=base_url+login_path
upload_url=base_url+upload_path

filename_to_upload ='layer_to_publish.tiff'
mime_tipe = 'image/tiff'

myfilepath = processing.getObject(layer_data).dataProvider().dataSourceUri()
(myDirectory,nameFile) = os.path.split(myfilepath)
abs_path = myDirectory + '/' + nameFile


print "Authenticate against CSRF Authentication, 3 steps..."
print "1/3 - First GET to retrieve the CSRFToken"
client=requests.session()
client.get(login_url)
csrftoken= client.cookies['csrftoken']
print "2/3 - Using the previously retrieved CSRFToken I perform a post"
login_data = dict(username=user, password=password, csrfmiddlewaretoken=csrftoken, next='/')
r = client.post(login_url, data=login_data, headers=dict(Referer=login_url))
csrftoken=r.cookies['csrftoken']
print "3/3 - perform login with the cookies configured"
client.get(upload_url)
csrftoken= client.cookies['csrftoken']
login_data = dict(username=user, password=password, csrfmiddlewaretoken=csrftoken, next='/')
print 'User: ' + user+ 'Authenticated!'


# ?????
#dict_user = d = {"users":{"AnonymousUser":{"view_resourcebase","download_resourcebase"}},"groups":{}}

print "preparing the POST HTTP request to send..."
json_user = json.loads('"{\\"users\\":{},\\"groups\\":{}}"')
login_data = dict(username=user, password=password, csrfmiddlewaretoken=csrftoken, next='/', permissions=json_user, abstract=abstract, layer_title=layer_title, charset='UTF8')
#upload = {'base_file': ('image.tiff', open(abs_path, "rb"), 'image/tiff')}
print abs_path

upload = {'base_file': (filename_to_upload, open(abs_path, "rb"), mime_tipe)}
print "...POST the request..."
r = client.post(upload_url, files=upload, data=login_data)

try:
    response_json=json.loads(r.text)
except Exception:
    raise ValueError("Error reading the response, the Layer may not be published...\nCheck if the Geonode URL you provided is working and if the Credentials are valid...")
    
print ""
print "******************************************"
print "** Geonode URL of the published request **"
print "******************************************"
print "** " + (base_url+response_json['url'])
print "******************************************"