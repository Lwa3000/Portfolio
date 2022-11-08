'''
Description: A map showing the valcano locations and population of each country.
How to run: 1. Execute the program by: python3 app2_webmap.py
			2. Open up file created in browser: Map1.html
Features: 1. There are markets showing valcano locations. The color indicates the height of the valcano. Green for less than 1000m; orange for between 1000 and 3000m; red for greater than 3000m.
		  2. The color for each country represents the population of the country. Green for less than 10 millions; Orange for between 10 million and 20 millions; Red for greater than 20 millions.
		  3. There is layer country so you can hide/show the 'Valcano layer' or the 'Population layer'.
'''
import folium
import pandas
map = folium.Map(location=[38.58,-99.89], zoom_start=6)#, tiles="Mapbox Bright")
#Create a feature group, allows you to switch the layers on and off.
#This feature group is only for the Valcanoes/market layer
fgv=folium.FeatureGroup(name="Valcanoes")

data = pandas.read_csv("Volcanoes.txt")
#convert data frame to a list, because working on list is faster
lat=list(data["LAT"])
lon=list(data["LON"])
elev = list(data["ELEV"])

#make the icon color change based on the elevation. Folium doesn't do this. So I can do it with a function.
#need to create the function before using it.
def color_producer(elev):
	if elev < 1000:
		return 'green'
	elif 1000<= elev <3000:
		return 'orange'
	else:
		return 'red'

#to add multiple markers
#add elevation data to the popup window.
#This is the market layer
for lt, ln, el in zip(lat, lon, elev):
	#fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+" m", icon=folium.Icon(color=color_producer(el))))
	#This is a point layer, there's line layer(rivers) and polygons(represent areas)
	fgv.add_child(folium.CircleMarker(radius=5,location=[lt,ln],popup=str(el)+" m", fill_color=color_producer(el)))

#This is the Json layer
fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig'),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <10000000 else 'orange' if 10000000<= x['properties']['POP2005'] <20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
#create layer control: allow to show/hide a layer, has to be added after the Json layer is added as a child
map.add_child(folium.LayerControl())

map.save("Map1.html")

#lambda function
# l = lambda x: x**2
# ls(5)
