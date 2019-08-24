from osgeo import ogr

propertiesFile = "/home/russell/DisasterResponse/validateData/tl_2015_36_prisecroads.shp"


'''
Name: geom_type
Date 2019-08-20
Author: Russell Brown
Purpose: Read the Geometry Types

Vatiable: pathToData
'''
def geom_type(pathToData):
    shapefile = ogr.Open(pathToData)
    layer = shapefile.GetLayer()
    List = []
    for feature in layer:
        geometry = feature.GetGeometryRef()
        #print(geometry.GetGeometryName())
        List.append(geometry.GetGeometryName())
   
    
    return List

'''
Name: ValidateList
Date: 2019-08-24
Author: Russell Brown
Purpose check to make sure all data are equal to LineString, 
If all are equal to a LineString return true,
If not all LineString return False


Variables:
	geometryTypes: Is a List of all the different Geometry types that were in the shapefile being looked at.

'''
def ValidateList(geometryTypes):
	results = False
	if(geometryTypes.count(geometryTypes[0]) == len(geometryTypes) and geometryTypes[0]=="LINESTRING"):
		results = True	
	return results	

'''
Name: GetAll Points
Date: 2019-08-24
Author: Russell Brown
Purpose: To open up the shapefile and read all the points and store them into an array.

Variables: 
	pathToDate: used to read in all the data points and return them to the main method
	

'''
def GetAllPoints(pathToData):
	file = ogr.Open("my_shapefile.shp")
	shape = file.GetLayer(0)
	#sfirst feature of the shapefile
	feature = shape.GetFeature(0)
	first = feature.ExportToJson()
	print first



'''
Name:Main Method
Date:2019-08-24
Author:Russell Brown
Purpose: The main method used to call all the other methods.
'''
if __name__ == '__main__':
	dataTypes = geom_type(propertiesFile)
	results = ValidateList(dataTypes)
	GetAllPoints(propertiesFile)
	print(results)
	
