import requests
import json
import os
import zipfile

# ##############################
# GUI: The data entry form
#
# ##Geonode_URL=string http://host[:port]
#
# test-> ##Geonode_URL=string http://192.168.50.170:8000
##Geonode_URL=string http://[ip]:[port]
##User=string your_username
##Password=string your_password
##Vector_Layer=vector
##compute_vector=boolean False
##Raster_Layer=raster
##compute_raster=boolean False
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
is_raster = compute_raster
is_vector = compute_vector

if ((is_raster and is_vector) or (not is_raster and not is_vector)):
   raise ValueError('Exactly ONE checkbox must be filled, choose between compute_raster or compute_vector')

if (is_raster):
    layer_data = Raster_Layer
    data_type='raster'

if (is_vector):
    layer_data = Vector_Layer
    data_type='vector'

login_path='/account/login/?next=/'
upload_path='/layers/upload'

layer_title=Title
abstract=Abstract

base_url = Geonode_URL
login_url=base_url+login_path
upload_url=base_url+upload_path



myfilepath = processing.getObject(layer_data).dataProvider().dataSourceUri()
(myDirectory,nameFile) = os.path.split(myfilepath)
abs_path = myDirectory + '/' + nameFile


print 'Handle the 3 input format supported: Vector(shp) , Vector(zipped_shp), Raster(GeoTIFF)'

filename_to_upload = ""
mime_tipe = ""
if data_type == 'vector':
    filename_to_upload = "layer_to_publish.zip"
    mime_tipe = "application/zip"
    if '/vsizip/' in str(abs_path):
        abs_path=abs_path.split('|', 1)[0]
        abs_path = abs_path[8:]
        print "an archive has been found here: '"  + abs_path + "'"
    else:
        abs_path = zipLayer(myfilepath)
if data_type == 'raster':
    filename_to_upload ='layer_to_publish.tiff'
    mime_tipe = 'image/tiff'

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

print "...Request result:"
print(json_user)
print(r.text)


