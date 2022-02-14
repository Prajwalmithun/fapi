# for sending requests to the API

import requests

BASE_URL = "http://127.0.0.1:5000/"

data = [{"name": "how to make bike?", "likes": 130, "views": 1000}, 
        {"name": "how to make cycle?", "likes": 1000, "views": 104556},
        {"name": "how to make pizza?", "likes": 1098, "views": 104553}]


for x in range(len(data)):
    response = requests.put(BASE_URL + "video/" + str(x), data[x])
    print(response.json())

# # this video already exists
# response = requests.delete(BASE_URL + "video/0")
# print(response)

# # this video doesnt exists
# response = requests.delete(BASE_URL + "video/10")
# print(response)

# get method to query the video
response = requests.get(BASE_URL + "video/2")
print(response.json())


# get method to query the video that dont exists
response = requests.get(BASE_URL + "video/10")
print(response.json())

# Update the video

response = requests.patch(BASE_URL + "video/2", {'likes': 109})
print(response.json())

response = requests.get(BASE_URL + "video/2")
print(response.json())


# Delete the video

response = requests.delete(BASE_URL + "video/1")
print(response)

# Query all the videos
response = requests.get(BASE_URL + "video/0")
print(response.json())
response = requests.get(BASE_URL + "video/1")
print(response.json())
response = requests.get(BASE_URL + "video/2")
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