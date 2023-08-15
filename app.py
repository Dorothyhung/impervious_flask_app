from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# 1 - image ovverlay with gmplot
# import gmplot
# gmap = gmplot.GoogleMapPlotter(31.513503879050337, 74.33410182086186, 18)
# url='https://openclipart.org/download/247271/hombre-hello-remix-cyberscooty.svg'
# bounds = {'north': 32.51358166525338, 'south': 31.513210019476748, 'east': 74.33334500058436, 'west': 74.33283133607337}
# gmap.ground_overlay(url, bounds)
# gmap.draw("./templates/index.html")


# 2 - world map with folium image overlay
# import folium
# m = folium.Map(
#         location=[43.761539, -79.411079],
#         tiles="Stamen Toner",
#         zoom_start=11
#         )
# merc = "Mercator_projection_SW.png"
# img = folium.raster_layers.ImageOverlay(
#     name="Mercator projection SW",
#     image=merc,
#     bounds=[[-82, -180], [82, 180]],
#     opacity=0.6,
#     interactive=True,
#     cross_origin=False,
#     zindex=1
# )
# img.add_to(m)
# folium.LayerControl().add_to(m)
# m.save("templates/index.html")
# m

import folium
import rasterio as rio

#import gdal

path = "impervious_rendered.tif"
with rio.open(path) as src:
    boundary = src.bounds
    img = src.read()

clat = (34.7236241463 + 34.7833234084)/2
clon = (-84.5767920522 + -84.519140314)/2

m = folium.Map(location=[clat, clon], tiles='Stamen Terrain', zoom_start = 10)
folium.raster_layers.ImageOverlay(
    image=img[0],
    name='test',
    opacity=1,
    bounds=[[34.7236241463, -84.5767920522], [34.7833234084, -84.519140314]],
).add_to(m)

folium.LayerControl().add_to(m)
m.save('templates/index.html')
m
