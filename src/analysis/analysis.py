import geopy.distance
from math import sin, cos, sqrt, atan2, radians

def translate_coordinates(x):
    return

def calculate_distance(x,y):
    """
    Calculates the distance between two gps coordinates
    X should be a list of [long1, lat1]
    y should be a list of [long2, lat2]
    """
    # return geopy.distance.vincenty(x, y).km
    R = 6370
    lat1 = radians(x[0])  #insert value
    lon1 = radians(x[1])
    lat2 = radians(y[0])
    lon2 = radians(y[1])

    dlon = lon2 - lon1
    dlat = lat2- lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance
