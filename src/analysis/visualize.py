import os

from gmplot import GoogleMapPlotter
import pandas as pd


# We subclass this just to change the map type
# taken from: https://stackoverflow.com/a/54164812
class CustomGoogleMapPlotter(GoogleMapPlotter):
    def __init__(self, center_lat, center_lng, zoom, apikey='',
                 map_type='satellite'):
        super().__init__(center_lat, center_lng, zoom, apikey)

        self.map_type = map_type
        assert(self.map_type in ['roadmap', 'satellite', 'hybrid', 'terrain'])

    def write_map(self,  f):
        f.write('\t\tvar centerlatlng = new google.maps.LatLng(%f, %f);\n' %
                (self.center[0], self.center[1]))
        f.write('\t\tvar myOptions = {\n')
        f.write('\t\t\tzoom: %d,\n' % (self.zoom))
        f.write('\t\t\tcenter: centerlatlng,\n')

        # This is the only line we change
        f.write('\t\t\tmapTypeId: \'{}\'\n'.format(self.map_type))


        f.write('\t\t};\n')
        f.write(
            '\t\tvar map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);\n')
        f.write('\n')


def visualize(data_path, vis_path) -> None:
    """Create google maps render of path that is reported from gps"""
    initial_zoom = 16

    df_gps = pd.read_csv(data_path)

    lats = df_gps.lat
    lons = df_gps.lon

    gmap = CustomGoogleMapPlotter(
            lats[0],
            lons[0],
            initial_zoom,
            map_type='satellite')

    gmap.plot(lats, lons, 'cornflowerblue', edge_width=1)

    gmap.draw(vis_path)

def visualize_all(**config) -> None:

    for folder in config["data_folders"]:
        vis_folder = folder.replace("data", "vis")

        if not os.path.exists(vis_folder):
            os.makedirs(vis_folder)

        for gps_csv in os.listdir(folder):
            data_path = folder + gps_csv
            vis_path = vis_folder + gps_csv.replace("csv", "html")
            visualize(data_path, vis_path)


