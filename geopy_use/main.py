from geopy.geocoders import Nominatim
from geopy.location import Location
import geocoder 

def get_current_gps_coordinates(ip: str = 'me') -> list:
    g = geocoder.ip(ip)
    return g.latlng if g.latlng else None

def get_position(latitude: float, longitude: float) -> Location:
    geolocator = Nominatim(user_agent="myapp/1")
    return geolocator.geocode(str(latitude)+","+str(longitude))
    

def main() -> None:
    coordinates = get_current_gps_coordinates()
    if coordinates:
        latitude, longitude = coordinates
        geolocator = get_position(latitude, longitude)
        print(latitude,longitude, geolocator)
    else:
        print("Unable to retrieve your GPS coordinates.")
        
if __name__ == '__main__':
    main()