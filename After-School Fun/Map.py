import folium
import geocoder

# Get the user's current location based on their IP address
g = geocoder.ip('me')  # 'me' gets the current device's location
latitude = g.latlng[0]  # Latitude
longitude = g.latlng[1]  # Longitude

# Create the map centered on the user's location
location = [latitude, longitude]
my_map = folium.Map(location=location, zoom_start=12)

# Save the map as an HTML file
my_map.save("user_location_map.html")
print("Map saved successfully!")
