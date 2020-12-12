import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import utm


def cep(**config):
    """Calculate circular error probable of gps coordinates"""
    df_gps = pd.read_csv(config["full_fixed_gps"])

    lats, lons = df_gps.lat, df_gps.lon
    utm_x, utm_y = convert_utm(list(zip(lats, lons)))

    # find delta "x" and "y"
    utm_x -= np.mean(utm_x)
    utm_y -= np.mean(utm_y)

    sigma_x, sigma_y = np.std(utm_x), np.std(utm_y)

    cep = 0.59 * (sigma_x + sigma_y)
    drms_gps = two_d_rms(utm_x, utm_y)

    plot_results(cep, drms_gps, utm_x, utm_y)

    return cep


def convert_utm(coords):
    """Convert latitude and longitude into UTM coordinates"""
    utm_x, utm_y = [], []
    # convert every coordinate pair into utm
    for lat, lon in coords:
        utm_coord = utm.from_latlon(lat, lon)
        utm_x.append(utm_coord[0])
        utm_y.append(utm_coord[1])

    return utm_x, utm_y


def two_d_rms(x, y):
    """Calculate 2DRMS for coordinates"""
    return 2 * np.sqrt(np.std(x)**2 + np.std(y)**2)


def plot_results(cep, drms, x, y):
    """Plot Coordiantes and respective circles"""
    center = (np.mean(x), np.mean(y))
    fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot

    # add circles
    circle_cep = plt.Circle(center, radius=cep, color='r', fill=True, alpha=0.15)
    circle_drms = plt.Circle(center, radius=drms, color='g', fill=True, alpha=0.15)
    ax.add_patch(circle_cep)
    ax.add_patch(circle_drms)

    # add points
    position = plt.scatter(x, y)

    plt.title("GPS Fixed Position")
    plt.xlabel("delta x (m)")
    plt.ylabel("delta y (m)")
    plt.legend([position, circle_cep, circle_drms],
               ["Distance From Average", "CEP (50%)", "2DRMS (95-98%)"])

    # fix axes
    ax.ticklabel_format(useOffset=False, style='plain')

    plt.axis('equal')

    plt.show()
    
