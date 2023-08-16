from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



import folium
import rasterio as rio

path = "impervious_rendered.tif"
with rio.open(path) as src:
    boundary = src.bounds
    img = src.read()

clat = (34.7236241463 + 34.7833234084)/2
clon = (-84.5767920522 + -84.519140314)/2

m = folium.Map(location=[clat, clon], tiles='Stamen Terrain', zoom_start = 13)
folium.raster_layers.ImageOverlay(
    image=img[0],
    name='test',
    opacity=1,
    bounds=[[34.7236241463, -84.5767920522], [34.7833234084, -84.519140314]],
).add_to(m)

# folium.LayerControl().add_to(m)
# m.save('templates/index.html')
# m
