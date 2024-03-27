"""
This is a module to get latitude and longitude (using geopy)
and transform that data in a readable position (using geocoder)

"""
from geopy.geocoders import Nominatim
from geopy.location import Location
import geocoder 

def get_current_gps_coordinates(ip: str = 'me') -> list:
    """Return a list with latitude and longitude values

    Args:
        ip (str, optional): The ip address that you want to check. Defaults to 'me'.

    Returns:
        list: A list with latitude and longitude values. [latitude, longitude]
    """
    g = geocoder.ip(ip)
    return g.latlng if g.latlng else None

def get_position(latitude: float, longitude: float) -> Location:
    """Return a readable position as an address

    Args:
        latitude (float): value for latitude
        longitude (float): value for longitude

    Returns:
        Location: A location with important methods such as
                    address, altitude, latitude, longitude, point, and raw
    """
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