from string import Template 

##Layer_name=string a_layer_name
##src_Datasource=file
##Geometry_type=string wkbPoint
##SRS=crs EPSG:4326
##Geometry_encoding=string wkt
##Geometry_field_name=string the_geom

##output_vrt_path=output file

tmpFolder='D:/work/data/cread/'

args = {
    'layer_name': Layer_name,
    'srcDatasource': src_Datasource,
    'geometry_type': Geometry_type,
    'srs': SRS,
    'geomEncoding': Geometry_encoding,
    'geometryFieldName': Geometry_field_name
}

template= "<OGRVRTDataSource>\n\t<OGRVRTLayer name=\"${layer_name}\">\n\t<SrcDataSource>${srcDatasource}</SrcDataSource>\n\t<GeometryType>${geometry_type}</GeometryType>\n\t<LayerSRS>${srs}</LayerSRS>\n\t<GeometryField encoding=\"${geomEncoding}\" field=\"${geometryFieldName}\" />\n\t</OGRVRTLayer>\n</OGRVRTDataSource>"

s = Template(template)
vrt_content = s.safe_substitute(**args)

print str(vrt_content)

vrt_path=tmpFolder + args['layer_name'] + '.vrt'
f=open(vrt_path, 'w')
f.write(vrt_content)
f.close()

output_vrt_path=vrt_path