"""
cleans in batches and moves cleaned data to gps_data assuming our the path to
our raw data looks something like this: '../data/raw/first_fix/'
"""
import pandas as pd


def clean_gps(**config) -> None:
    """Transfrom raw gps data into cleaned latitude and longitude csv"""
    df_gps = pd.read_csv(
        config["test_path"],
        index_col=None,
        header=None,
        names=['lat', 'lon', 'alt'])
    df_gps.lat = df_gps.lat.str.replace("lat=", "").astype(float)
    df_gps.lon = df_gps.lon.str.replace("lon=", "").astype(float)
    df_gps.alt = df_gps.alt.str.replace("alt=", "").astype(float)

    cleaned_file_path = (
        config["test_path"]
        .replace(".log", "_cleaned.csv")
    )
    df_gps.to_csv(cleaned_file_path, index=False)
