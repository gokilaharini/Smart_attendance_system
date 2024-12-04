from geopy.distance import geodesic
from shapely.geometry import Point, Polygon

# Define geofences
geofences = [
    {"latitude": 13.0475, "longitude": 80.1764, "radius": 500},  # Chennai, India
    {"latitude": 28.6139, "longitude": 77.2090, "radius": 1000},  # Delhi, India
]

# Check if a location is within a geofence
def is_within_geofence(location, geofence):
    point = Point(location["latitude"], location["longitude"])
    center = Point(geofence["latitude"], geofence["longitude"])
    distance = geodesic(point, center).meters
    return distance <= geofence["radius"]

# Function to handle geofence events (e.g., send notifications)
def handle_geofence_event(geofence):
    print(f"Entered geofence: {geofence}")  # Replace with your desired action

# Example usage
user_location = {"latitude": 13.0575, "longitude": 80.1764}  # Near Chennai
for geofence in geofences:
    if is_within_geofence(user_location, geofence):
        handle_geofence_event(geofence)

# For real-time monitoring, consider using a background service or task scheduler
# to periodically check user locations against geofences
