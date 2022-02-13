# This is the python file for creating a YouTube like API

from email import message
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

# app init
app = Flask(__name__)

# api wrap over the app
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required",required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=str, help="Likes on the video is required", required=True)

videos = {}

# aborting if video not present with us
def abort_if_video_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find the video...")

# if users add the video that already exists
def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video already present with this ID...")


# Resource def
class Video(Resource):
    # GET req
    # just returning the videos
    def get(self, video_id):
        abort_if_video_doesnt_exist(video_id)
        return videos[video_id]

    # PUT req
    # adding new videos
    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        return {video_id: args}

# register the resource
api.add_resource(Video, "/video/<int:video_id>")


# running the app
if __name__ == "__main__":
    app.run(debug=True)