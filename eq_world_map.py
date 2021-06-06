import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

#Extract all earthquakes
all_eq_dicts = all_eq_data['features']

#Extract all magnitudes and location data(latitute and longitude)
mags, lons, lats, hover_txts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_txts.append(title)

#Map the earthquakes
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_txts,
    'marker' : {
        'size' : [5*mag for mag in mags],
        'color' : mags,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Magnitude'}
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig= {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='global_earthquakes.html')