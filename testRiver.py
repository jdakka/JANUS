
# for the geographic data handeling
try:
  from osgeo import ogr
  print 'Import of ogr from osgeo worked.  Hurray!\n'
except:
  print 'Import of ogr from osgeo failed\n\n'
  
from osgeo import gdal  

# for the transformation between projections
from osgeo import osr
import os
if not os.environ['GDAL_DATA'] == 'C:\Program Files\GDAL\gdal-data':
    os.environ['GDAL_DATA'] = 'C:\Program Files\GDAL\gdal-data'
if 'GDAL_PATH' not in os.environ:
    os.environ['GDAL_PATH'] = 'C:\Program Files\GDAL'
    
# for formating to JSON, do: conda install -c ioos geojson    
#from geojson import Polygon

  #%%

driver = ogr.GetDriverByName('ESRI Shapefile')
os.chdir('C:\Janus\Git\JANUS')
fname = 'Rivers.shp'  

if not os.path.isfile(fname):
    raise IOError('Could not find file ' + str(fname))
source = ogr.Open(fname, gdal.GA_Update)
if source is None:
    raise IOError('Could open file ' + str(fname))

layer = source.GetLayer()

#%% get name of the fields of the shapefile 
ldefn = layer.GetLayerDefn()
schema = []
for n in range(ldefn.GetFieldCount()):
    fdefn = ldefn.GetFieldDefn(n)
    schema.append(fdefn.name)
print schema

#%%

nameOI = 'Mackenzie' # the river name we are interested in
obID = []
for feature in layer:
    if feature.GetField("name")==nameOI: # 
        obID.append(feature.GetField("OBJECTID"))
#        print feature.GetField("name")
layer.ResetReading()

# get the geometry of the river and buffer, thus from a line to a polygon
bufferDist = 1e3 # in meters

# transform from projection to lat-long 
inSpatialRef = layer.GetSpatialRef() # North_Pole_Stereographic
outSpatialRef = osr.SpatialReference() # WGS 84
outSpatialRef.SetWellKnownGeogCS("WGS84")
# print inSpatialRef.ExportToPrettyWkt()
# print outSpatialRef.ExportToPrettyWkt()

coordTrans = osr.CoordinateTransformation(inSpatialRef, outSpatialRef)

poly = ogr.Geometry(ogr.wkbMultiPolygon)
for i in obID:
    feature = layer.GetFeature(obID[2])
    geom = feature.GetGeometryRef()
    # make a buffer
    buff = geom.Buffer(bufferDist)
    
    # transform to lat,lon
    buff.Transform(coordTrans)
    
    # join with other buffers
    poly = poly.Union(buff)

# cut here in smaller polygons if needed


# transform to geoJSON object
geojson = poly.ExportToJson()

#%%
#print layer.GetExtent()
#print layer.GetDescription()
#print layer.GetFeatureCount()
#print layer.GetSpatialRef()
#
#for feature in layer:
#    print feature.GetField("STATE_NAME")