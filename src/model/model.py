import glob
import os
import re

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt

# Calculates distance(in feet) between two pairs of coordinates
# Note: Assumes gps outputs coordinates in degree not radian. Distance formula based on Vincenty's alg and
# assuming earth is sphere. Formula not as accurate as assuming earth is spheroid but should be pretty accurate/
def distance(lat1, lon1, lat2, lon2) -> float:

    #convert latitiude and longitude to spherical coords
    #comment out if coords are already in radians
    lat1, lon1 = np.deg2rad(lat1), np.deg2rad(lon1)
    lat2, lon2 = np.deg2rad(lat2), np.deg2rad(lon2)
    
    # average radius of earth in feet
    r = 20890565.9449 
    
    p1 = 0.5*np.pi-lat1
    p2 = 0.5*np.pi-lat2
    a = np.sin(p1)*np.sin(p2)*np.cos(lon1-lon2)+np.cos(p1)*np.cos(p2)
    
    return r * np.arccos(a)

# calculates root mean square error between a list of predictions and list of actual
def rmse(expected, actual) -> float:    
    
    total_preds = len(expected)
    sum_error = 0.0
    
    for i in range(total_preds):
        squared_error = (actual[i]-expected[i])**2
        sum_error += squared_error
    return sqrt(sum_error/float(total_preds))

# Takes in a path like: "../../data/gps_data/first_fix"
# Finds dist between start and end coordinates (first and last entry in each cleaned csv respectively).
# Compiles a df with batch name, run name, start coord, end coord, ground truth, calc'ed dist, and rmse
# FOR THE WHOLE BATCH rather than single run
def calc_distances(path) -> pd.DataFrame():
    
    ground_truth = int(path.split("../../data/gps_data/", 1)[1].replace("ft",""))
    files = glob.glob(path + "/*.csv")
    df_dist = pd.DataFrame(columns = ['batch', 'run','start_lat_lon','finish_lat_lon','expected_dist','actual_dist','rmse'])
    
    for file in files:
        df = pd.read_csv(file)
        start = df.iloc[0]
        finish = df.iloc[-1]
        calc_dist = distance(start.lat, start.lon, finish.lat, finish.lon)
        name = re.search('(?:[^/](?!\/))+(?=_cleaned.csv)', file)
        batch = re.search('(?:\/gps_data\/)(.*(?=\/))', file)
        df_dist = df_dist.append({'batch': batch.group(1),'run' : name.group(), 'start_lat_lon': (start.lat, start.lon), 
                                  'finish_lat_lon': (finish.lat, finish.lon), 'expected_dist' : ground_truth, 
                                  'actual_dist' : calc_dist}, 
                                 ignore_index = True)
    df_dist.rmse = rmse(df_dist.expected_dist, df_dist.actual_dist)

    return df_dist

def compile(path):
    
    all_folders = glob.glob(os.path.join(path, '*'))
    for folder in all_folders:
        df = calc_distances(folder)
        df.to_csv("../../data/gps_data/rmse_all_batches.csv", mode="a")
    
