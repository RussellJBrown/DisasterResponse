import geopandas as gpd


def displayData(dataPath):
    for layer in dataPath:
        shape = gpd.read_file(layer)
        shape.plot()