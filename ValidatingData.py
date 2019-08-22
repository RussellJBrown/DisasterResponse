from osgeo import ogr

propertiesFile = "/home/russell/Documents/sampleData/Canada.shp"

def helloworld():
   print("helloworld")

'''
Name: geom_type
Date 2019-08-20
Author: Russell Brown
'''
def geom_type(pathToData):
    shapefile = ogr.Open(pathToData)
    layer = shapefile.GetLayer()
    List = []
    for feature in layer:
        geometry = feature.GetGeometryRef()
        print(geometry.GetGeometryName())
        List.append(geometry.GetGeometryName)
    return List

def ValidateList():


if __name__ == '__main__':
    helloworld()
    dataTypes = geom_type(propertiesFile)
    ValidateList()
