import folium





def createMapaPlot(ubicacion):
    m = folium.Map(location=ubicacion, 
            zoom_start=5,
            tiles='https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
            attr='&copy; <a href="https://carto.com/attributions">CARTO</a>')
    m.save('map.html')


createMapaPlot((40.54419400668234, -102.93430316168637))