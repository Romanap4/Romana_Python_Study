# def main():
#     coordinates = (42.376, -71.115)
#     latitude, longitude = coordinates
#     print(f"Latitude: {latitude}")
#     print(f"Longitude: {longitude}")

# main()

# print(f"Latitude: {coordinates[0]}")
# print(f"Longitude: {coordinates[1]}")

# Instead of finding values by using the index, you can unpack the tuple as shown in the code within the main() function.

# Checking how much space each of the following data structures (a tuple and a list) takes up in memory:

import sys

def main():
    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")
    
main()
