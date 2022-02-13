# Day 1

## Theory part

- Learnt about what is an API, advantages of API, types of APIs and surface level glance on API architecture.

## Coding part 

- Build 1st hello world API

- JSON exposed

- requesting end points using "requests" module , "httpie" command line, curl "command" line

# Day 2

- Getting parameters from the users and returing it back

- Started with creating video API (video ID = identify the id, likes = how ,many likes for this video, views = how many views for this video)

- Users normally give video_id, but we need to parse more variables wrt to that video like views, description, likes, dislikes, data created etc... so reqparse is helpful

- Aborting if the video already exists while adding new video AND abort if the video doesnt exists while requesting.