import folium

# Define the location coordinates (latitude and longitude)
latitude = 43.7  # Toronto latitude
longitude = -79.42  # Toronto longitude
location = [latitude, longitude]  # Combine into a list

# Create the map centered on the location
my_map = folium.Map(location=location, zoom_start=12)

try:
    my_map.save("simple_map.html")
    print("Map saved successfully!")
except Exception as e:
    print(f"Error saving the map: {e}")
