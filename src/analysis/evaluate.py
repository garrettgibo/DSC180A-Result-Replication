import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def cep(**config):
    """Calculate circular error probable of gps coordinates"""
    df_gps = pd.read_csv(config["full_fixed_gps"])

    lats, lons = df_gps.lat, df_gps.lon
    cart_x, cart_y = df_gps.x, df_gps.y

    # find delta "x" and "y"
    lats -= np.mean(lats)
    lons -= np.mean(lons)
    cart_x -= np.mean(cart_x)
    cart_y -= np.mean(cart_y)

    sigma_lat, sigma_lon = np.std(lats), np.std(lons)
    sigma_lat_c, sigma_lon_c = np.std(cart_x), np.std(cart_y)

    # cep equation
    cep = 0.59 * (sigma_lat + sigma_lon)
    cep_c = 0.59 * (sigma_lat_c + sigma_lon_c)

    drms_gps = two_d_rms(lats, lons)
    drms_car = two_d_rms(cart_x, cart_y)

    # plot_results(cep, drms_gps, lats, lons)
    plot_results(cep_c, drms_car, df_gps.x, df_gps.y)

    return cep


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
    plt.legend([position, circle_cep, circle_drms],
               ["Distance From Average", "CEP (50%)", "2DRMS (95-98%)"])

    # fix axes
    ax.ticklabel_format(useOffset=False, style='plain')

    plt.axis('equal')

    # plt.show()
    
