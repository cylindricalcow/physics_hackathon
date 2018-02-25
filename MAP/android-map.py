import pandas as pd
import folium
import android
import time
#import webbrowser, os.path

droid = android.Android()

#droid.makeToast("fetching GPS data")
map = folium.Map(location=[40.1106, -88.2073], zoom_start=12,tiles="Champaign")
map # display the map,  I can save it to a html file and display it
#map.save(outfile='map.html')
#webbrowser.open("file:///" + os.path.abspath('map.html'))

droid.startLocating()
print("start gps-sensor...")

while True:
    event = droid.eventWaitFor('location',10000).result
    if event['name'] == "location":
        try:
            lat = str(event['data']['gps']['latitude'])
            lng = str(event['data']['gps']['longitude'])
        except KeyError:
            lat = str(event['data']['network']['latitude'])
            lng = str(event['data']['network']['longitude'])    

        if lat and lng:
            folium.Marker([lat, lng], popup="current").add_to(map)
            map # display the map, I can save it to a html file and display it
            #map.save(outfile='map.html')
            #webbrowser.open("file:///" + os.path.abspath('map.html'))
    time.sleep(5)

print("stop gps-sensor...")
droid.stopLocating()

