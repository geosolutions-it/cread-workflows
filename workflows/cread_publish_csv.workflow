.NAME:Publish CSV
.GROUP:C-READ
.ALGORITHM:gdalogr:convertformat
.PARAMETERS:{"OPTIONS": "", "FORMAT": 0}
.MODE:Normal
.INSTRUCTIONS:
!INSTRUCTIONS
.ALGORITHM:gdalogr:executesql
.PARAMETERS:{"SQL": "select * from OUTPUTLAYER where [attribute]='[value]'"}
.MODE:Normal
.INSTRUCTIONS:
!INSTRUCTIONS
.ALGORITHM:script:publishvector
.PARAMETERS:{"UserName": "admin", "StoreName": "police_station_wgs84", "Password": "geoserver", "DomainName": "192.168.50.169:8080"}
.MODE:Normal
.INSTRUCTIONS:
!INSTRUCTIONS
