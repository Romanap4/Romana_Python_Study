# APIs, "application program interfaces", allow you to connect to the code of others
# type "pip install requests" in the terminal -> requests is a package that allows your program to behave as a web browser would
# Visit https://itunes.apple.com/search?entity=song&limit=1&term=weezer in your browser to access the Apple iTunes API; a text file will be downloaded
# This URL was constructed by reading Apple's API documentation; the query is looking for a song, with a limit of one result, that relates to a term called weezer
# The format in the downloaded text file is called JSON, a text-based format that is used to exchange text-based data between applications -> Apple is providing a JSON file that we could interpret in our own Python program

# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response.json())

# The returned value will be stored in response and it is a JSON file
# Python has a built-in JSON library that can help us interpret the data received

# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))

# json.dumps is implemented such that it utilizes indent to make the output more readable
# Inside the output there is a dictionary called results containing numerous keys
# Modifying the code to output just the trackName value

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
