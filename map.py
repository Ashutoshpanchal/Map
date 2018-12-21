import folium
import pandas as pd


df= pd.read_csv("val.txt")
#print(df)
lat = list(df["LAT"])
lon= list(df["LON"])
eal =list(df["ELEV"])

def color_change(el):
   if el<1000:
      return "green"
   elif 1000<= el <3000 :
      return "blue"
   else :
      return "red"
   
map=folium.Map(location=[80,-180],zoom_start=3,tiles="Mapbox Bright")#lag= -90 to 90 / long= -180 to 180
fg=folium.FeatureGroup(name="My Map")

for la,ln,el in zip(lat,lon,eal):
   fg.add_child(folium.CircleMarker(location=[la,ln],popup=str(el)+"m",tooltip="click on it"))#input(enter the name)/,icon=folium.Icon(color=color_change(el)



   
#fg.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig"),style_function=lambda x: {"fillColor":"red" if x ["properties"]["POP2005"]<10000000
#else "orange" if 10000000 <= x ["properties"]["POP2005"] < 20000000 else "red"}))


fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'),
style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))

   
map.add_child(fg)
map.save("map.html")
