
# coding: utf-8

# In[213]:

import folium

markers = []

#Define coordinates of where we want to center our map, where user is
uiuc_coords = [40.1100, -88.2272]
person_coords = [40.1100, -88.2272]

#Create the map
my_map = folium.Map(location = uiuc_coords, zoom_start = 18)


# In[214]:

def PlaceMarkers(coords):
    '''
    Populates map with markers in list of specified locations.
    coords: a list of lat/long coordinates
    '''
    for coord in coords:
        folium.CircleMarker(coord, radius = 7, color = "#800000", fill = True).add_to(my_map)
    return None

# creates CircleMarker where player is
folium.CircleMarker(person_coords, radius = 7, color = "#0A8A9F", popup = "Your position", fill = True).add_to(my_map)
   


# In[215]:

# Function for placing monsters on the map in DM Mode

def PlaceMonster(map_object):
    '''
    map_object: folium map object
    
    One click places monster, double click removes monster
    '''
    my_map.add_child(folium.ClickForMarker())
    return my_map

my_map

#Problem: I don't know how to stop ClickForMarker


# In[217]:

my_map.save('dd_map.html')


# In[218]:

my_map


# In[ ]:

campus_boundary_json = {
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


# In[ ]:



