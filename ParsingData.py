import sys

'''
Name: ParsedData
Date: 2019-08-25
Author: Russell Brown
Purpose: This method gets passed a bunch of information through an array.
This method parses through these arrays searching for the coordinated data.
'''
def ParseData(mainData):
	geometryData = [[]]
	i = 0
	for features in mainData:
		maintag = '{"type": "Feature", "geometry": {"type": "LineString", "coordinates": ['
		coordinates = features.split(maintag)[1]
		LineCoordinates = coordinates.split(",")
		tempGeometryData = []
		for point in LineCoordinates:			
			point = point.replace("[","")
			point = point.replace("]","")
			point = point.replace("'","")
			point = point.replace("}","")
			point = point.replace("{","")
			point = point.replace("","")
			try:
				pointInt = float(point)
				if(isinstance(pointInt, float)):
					tempGeometryData.append(pointInt)	 
			except: 
				pass
		geometryData.append(tempGeometryData)

	return geometryData
