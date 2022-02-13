# for sending requests to the API

import requests

BASE_URL = "http://127.0.0.1:5000/"

requests.get(BASE_URL + "video/1")

input()

response = requests.put(BASE_URL + "video/2", {"name": "how to make bike?", "likes": 10, "views": 10000})

input()

print(response.json())



# if using command line

# GET
# $ curl localhost:5000/video/1

# POST [NOT working]
# $ curl -X POST localhost:5000/videos/1?name=how&views=100000&likes10243

# PUT [NOT working]
# $ curl -X PUT localhost:5000/videos/1

# DELETE
# $ curl -X DELETE localhost:5000/videos/1 