import folium
import requests
import polyline

def create_map():
    # Start and End Coordinates (Default)
    start_coords = [45.327159, -75.587883]  # Ottawa, ON
    end_coords = [45.428, -75.6992]    # Another point in Ottawa, for example


    # Create the map centered on the start location
    my_map = folium.Map(location=start_coords, zoom_start=14)

    # Plot the start and end points
    folium.Marker(location=start_coords, popup="Start", icon=folium.Icon(color="green")).add_to(my_map)
    folium.Marker(location=end_coords, popup="End", icon=folium.Icon(color="red")).add_to(my_map)

    # Request the directions from the OSRM API
    osrm_url = f"http://router.project-osrm.org/route/v1/driving/{start_coords[1]},{start_coords[0]};{end_coords[1]},{end_coords[0]}?overview=full&geometries=polyline"
    response = requests.get(osrm_url)
    data = response.json()

    # Extract the route geometry (polyline)
    route = data['routes'][0]['geometry']
    decoded_route = polyline.decode(route)

    # Extract distance and duration
    distance = data['routes'][0]['legs'][0]['distance'] / 1000  # Convert meters to kilometers
    duration = data['routes'][0]['legs'][0]['duration'] / 60  # Convert seconds to minutes

    # Add the route to the map
    folium.PolyLine(decoded_route, color="blue", weight=5).add_to(my_map)

    # Add distance and time as a popup at the start point
    folium.Marker(
        location=start_coords, 
        popup=f"Distance: {distance:.2f} km\nDuration: {duration:.2f} mins",
        icon=folium.Icon(color="blue")
    ).add_to(my_map)

    # Save the map as an HTML file
    my_map.save("enhanced_map.html")
    print("Map with directions saved successfully as 'enhanced_map.html'.")

if __name__ == "__main__":
    print("Creating map...")
    create_map()