import math
import pandas as pd 
import glob
import os

# Transforms latitude and longitude into a cartesian x
# coordinate
def get_x(ellps, lat, lon, h) -> Float:
    """
    Compute the Geocentric (Cartesian) Coordinates X, Y, Z
    given the Geodetic Coordinates lat, lon + Ellipsoid Height h
    """
    wgs84 = (6378137, 298.257223563)
    a, rf = ellps
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    N = a / math.sqrt(1 - (1 - (1 - 1 / rf) ** 2) * (math.sin(lat_rad)) ** 2)
    X = (N + h) * math.cos(lat_rad) * math.cos(lon_rad)
    return X

# Transforms latitude and longitude into a cartesian y
# coordinate
def get_y(ellps, lat, lon, h) -> Float:
    """
    Compute the Geocentric (Cartesian) Coordinates X, Y, Z
    given the Geodetic Coordinates lat, lon + Ellipsoid Height h
    """
    wgs84 = (6378137, 298.257223563)
    a, rf = ellps
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    N = a / math.sqrt(1 - (1 - (1 - 1 / rf) ** 2) * (math.sin(lat_rad)) ** 2)
    Y = (N + h) * math.cos(lat_rad) * math.sin(lon_rad)
    return Y
    
# Takes in a path that is a file and returns a dataframe of the file including
# a x coordinate columnn and y coordinate column
def cartesian_conversion(path) -> pd.DataFrame():
    df = pd.read_csv(path)
    df['x'] = df2.apply(lambda row: get_x(wgs84, row.lat, row.lon, row.alt), axis =1)
    df['y'] = df2.apply(lambda row: get_y(wgs84, row.lat, row.lon, row.alt), axis =1)
    return df

# Takes in the fixed_all.csv and adds two new columns:
# the x and y coordinates of latitiude and longitude 
def transform_fixed_cartesian() -> None:
    path = "../../data/fixed_all.csv"
    df = cartesian_conversion(path)
    new_file_path = "../../data/fixed_all_cartesian.csv"
    df.to_csv(new_file_path, index=False)


