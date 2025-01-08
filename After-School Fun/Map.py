import folium
import requests

# Define the starting and ending coordinates (latitude, longitude)
start_coords = [45.4215, -75.6972]  # Ottawa, ON
end_coords = [45.428, -75.6992]    # Another point in Ottawa, for example

# Create the map centered on the start location
my_map = folium.Map(location=start_coords, zoom_start=14)

# Plot the start and end points
folium.Marker(location=start_coords, popup="Start").add_to(my_map)
folium.Marker(location=end_coords, popup="End").add_to(my_map)

# Request the directions from the OSRM API
osrm_url = f"http://router.project-osrm.org/route/v1/driving/{start_coords[1]},{start_coords[0]};{end_coords[1]},{end_coords[0]}?overview=full&geometries=polyline"
response = requests.get(osrm_url)
data = response.json()

# Extract the route geometry (polyline)
route = data['routes'][0]['geometry']

# Decode the polyline into a list of lat, lon coordinates
import polyline
decoded_route = polyline.decode(route)

# Add the route to the map
folium.PolyLine(decoded_route, color="blue", weight=5).add_to(my_map)

# Save the map as an HTML file
my_map.save("directions_map.html")
print("Map with directions saved successfully!")
