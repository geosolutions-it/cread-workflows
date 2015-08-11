import urllib
import httplib2

class GeonodeManager:
        'A class use to invoke Geonode API'
        _domainName = ""
        _username = ""
        _password = ""
        
        def __init__(self, username, password, domainName="localhost:8000"):
            if domainName == "":
                    print "No domain name provided, setting the default one (localhost:8000)"
                    domainName = "localhost:8000"
            if username == "":
                    raise NameError("No username provided!")
            if password == "":
                    raise NameError("No password provided!")
            self._domainName = domainName
            self._username = username
            self._password = password
        
        def publish_datastore(self, file_absolute_path, store_name):
            args = {'workspace':'geonode', 'storename':store_name, 'storeType':'datastores', 'extension':'shp', 'content-type':'application/zip'}
            self._publish_store(file_absolute_path, store_name, **args)
            
        def publish_coveragestore(self, file_absolute_path, store_name):
            args = {'workspace':'geonode', 'storename':store_name, 'storeType':'coveragestores', 'extension':'geotiff', 'content-type':'image/tiff'}
            self._publish_store(file_absolute_path, store_name, **args)
            
        def _publish_store(self, file_absolute_path, store_name, **kwargs):
            if file_absolute_path == "":
                    raise NameError("No absolute path for the file to upload has been provided...")
            if store_name == "":
                    raise NameError("No store name has been provided...")     
            print "Loading the file to upload..."
            f = open(file_absolute_path, "rb")
            chunk = f.read()
            f.close()
            print "...file successfully loaded!"
            
            headers = {
                    "Content-type": kwargs['content-type'],
                    "Accept": "text/plain"
            }
            h = httplib2.Http(".cache")
            h.add_credentials(self._username, self._password)
            #data = urllib.urlencode({"name":"test"})
            print "Calling the REST service..."
            url = self._build_URL(**kwargs)
            print "Calling the service endpoint: '" + url + "'"
            response, content = h.request(url, "PUT", chunk, headers)
            print "Headers are: '" + headers['Content-type'] + "'"
            print "The Response is: "
            print response
            print "The Content is : '"
            print content
            print "'"
        
        def _build_URL(self, **kwargs):
            baseUrl = "http://" + self._domainName + "/geoserver/rest"
            restPath1 = "/workspaces"
            restPath2 = "/" + kwargs['workspace']
            restPath3 = "/" + kwargs['storeType']
            restPath4 = "/" + kwargs['storename']
            file = "/file."
            url = baseUrl + restPath1 + restPath2 + restPath3 + restPath4 + file + kwargs['extension']
            return url