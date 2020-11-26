"""
cleans in batches and moves cleaned data to gps_data assuming our the path to
our raw data looks something like this: '../data/raw/first_fix/'
"""
import glob
import os
import pandas as pd


def clean_gps(path):
    """Transfrom raw gps data into cleaned latitude and longitude csv"""
    # make a new folder inside temp to hold cleaned data
    # for each batch
    new_folder = path.split("../data/raw/", 1)[1]
    os.mkdir("../data/gps_data/"+new_folder)
    all_raw_files = glob.glob(path + "/*.log")

    for file in all_raw_files:
        print("Cleaning raw data at", file)

        df_gps = pd.read_csv(file, index_col=None, header=None, names=['lat', 'lon', 'alt'])
        df_gps.lat = df_gps.lat.str.replace("lat=", "").astype(float)
        df_gps.lon = df_gps.lon.str.replace("lon=", "").astype(float)
        df_gps.alt = df_gps.alt.str.replace("alt=", "").astype(float)

        cleaned_file_path = file.replace(".log", "_cleaned.csv").replace("../data/raw", "../data/gps_data")
        df_gps.to_csv(cleaned_file_path, index=False)
    print("Cleaned csv for all raw data inside", new_folder, " at ", "../data/gps_data/"+new_folder)
