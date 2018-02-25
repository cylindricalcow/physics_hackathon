
# coding: utf-8

# In[131]:

import folium

#Define coordinates of where we want to center our map, place people
uiuc_coords = [40.1100, -88.2272]
person_coords = [40.1100, -88.2272]

#Create the map
my_map = folium.Map(location = uiuc_coords, zoom_start = 18)

#Creates markers
folium.CircleMarker(person_coords, radius = 7, color = "#0A8A9F", popup = 'Your position', fill = True).add_to(my_map)

def buffer(point, radius):
    return folium.Circle(point, radius = radius, color = "#ffff00", fill = True).add_to(my_map)

buffer(person_coords,18)


folium.LayerControl().add_to(my_map)


# In[132]:

campus_json = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -88.23866844177246,
              40.09773821446634
            ],
            [
              -88.21892738342285,
              40.09803366543276
            ],
            [
              -88.21918487548827,
              40.116611671198925
            ],
            [
              -88.23884010314941,
              40.116480395674515
            ],
            [
              -88.23866844177246,
              40.09773821446634
            ]
          ]
        ]
      }
    }
  ]
}


# In[133]:

#Display the map
my_map

### Saves map in file
#map_osm.save('/tmp/map.html')


# In[ ]:




# In[ ]:

## Function for placing a monster on a map in DM Mode
# def PlaceMonster(map, MonsterName):
#     folium.CircleMarker(uiuc_coords, popup= MonsterName).add_to(map)
#     map.add_child(folium.ClickForMarker(popup='Waypoint'))
#     return None


# click on map and shows lat long coords
# my_map.add_child(folium.LatLngPopup())

