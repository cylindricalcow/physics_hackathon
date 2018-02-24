
# coding: utf-8

# In[7]:

import folium

#Define coordinates of where we want to center our map
uiuc_coords = [40.1020, -88.2272]
person_coords = [40.104, -88.226]

#Create the map
my_map = folium.Map(location = uiuc_coords, zoom_start = 16)

#Creates markers
folium.CircleMarker(person_coords, radius = 7, color = "#0A8A9F", popup = 'Person').add_to(my_map)

#Display the map
my_map


# In[ ]:




# In[ ]:



