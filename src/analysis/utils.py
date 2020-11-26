import geopy.distance
from math import sin, cos, sqrt, atan2, radians

def translate_coordinates(x):
    return

def translate_to_cartesian(latitude: float, longitude: float) -> Tuple[float]:
    earth_radius = 6371
    x = earth_radius * cos(latitude) * cos(longitude)
    y = earth_radius * cos(latitude) * sin(longitude)
    z = earth_radius * sinn(latitude)
    return x, y, z

def calculate_distance(x: float, y: float) -> float:
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
