# import pandas as pd


# def clean_gps(**config) -> pd.DataFrame:
#     """Clean raw gps data and transform into datafram with columns latitude and
#     longitude.
#     """
#     df_gps = pd.read_csv(config["gps_raw_data"])
#     df_gps.columns = ["lat", "lon", "alt"]
#     df_gps.lat = df_gps.lat.str.replace("lat=", "").astype(float)
#     df_gps.lon = df_gps.lon.str.replace("lon=", "").astype(float)
#     df_gps.alt = df_gps.alt.str.replace("alt=", "").astype(float)

#     cleaned_path = config["gps_raw_data"].replace("raw", "temp").replace("log", "csv")
#     print(cleaned_path)
#     df_gps.to_csv(cleaned_path, index=False)


import pandas as pd
import glob
import os

# cleans all folders inside data/raw and creates csv of
# cleaned data to gps_data under a folder with the same
# name as it is in data/raw
# assumes the path to our raw data looks something
# like this: '../data/raw/first_fix/'

def clean_gps(path) -> pd.DataFrame:

    all_raw_folders = glob.glob(os.path.join(path, '*'))

    for folder in all_raw_folders:
        folder_path = folder + "/"

        if os.path.isdir(folder_path):
            # make new folder inside gps_data with same batch name
            new_folder_path = "../../data/gps_data/" + folder_path.split("../../data/raw/",1)[1]
            os.mkdir(new_folder_path)

            # clean files inside batch and send to folder under same batch name in gps_dats
            all_raw_files = glob.glob(folder_path+ "/*.log")
            for file in all_raw_files:
                print("Cleaning raw data at", file)

                df_gps = pd.read_csv(file, index_col=None, header=None, names=['lat', 'lon', 'alt'])
                df_gps.lat = df_gps.lat.str.replace("lat=", "").astype(float)
                df_gps.lon = df_gps.lon.str.replace("lon=", "").astype(float)
                df_gps.alt = df_gps.alt.str.replace("alt=", "").astype(float)

                cleaned_file_path = file.replace(".log", "_cleaned.csv").replace("../data/raw", "../data/gps_data")
                df_gps.to_csv(cleaned_file_path, index=False)
            print("Cleaned csv for all raw data inside", folder_path, " at ", "../data/gps_data/" + new_folder_path)
