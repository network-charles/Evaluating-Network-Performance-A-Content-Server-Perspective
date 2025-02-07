import math
 
# https://en.wikipedia.org/wiki/Haversine_formula
# https://www.movable-type.co.uk/scripts/latlong.html
 
def distance(origin, destination):
 
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km
 
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
 
    return d
 
origin = (6.5244, 3.3792)              # Lagos
destination = (37.3387, 121.8853)         
 
print("Distance in KM : {} ".format(distance(origin, destination)))
print("Distance in MI : {}".format(
 
    distance(
        origin, destination
    )*0.621371
 
))
