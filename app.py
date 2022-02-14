# This is the python file for creating a YouTube like API

from cgitb import reset
from email import message
import os
from urllib import request
from flask import Flask, render_template, url_for
from flask_restful import Api, Resource, marshal_with, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from apispec import APISpec
from marshmallow import Schema
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs
import random
import string

# app init
app = Flask(__name__)

# database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='MockTube API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})

docs = FlaskApiSpec(app)

# random names generation for video names
rnames = ''.join(random.choices(string.ascii_lowercase, k=6))


# creating home page, this just contains button to the API docs
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")




class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False) # entry should always have a name
    likes = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"


#db.create_all()

# api wrap over the app
api = Api(app)


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required")
video_put_args.add_argument("views", type=int, help="Views of the video is required")
video_put_args.add_argument("likes", type=str, help="Likes on the video is required")


video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video is required")
video_update_args.add_argument("likes", type=str, help="Likes on the video is required")


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# Resource def
class Video(MethodResource,Resource):
    @doc(description='Get details of the video', tags=['Query'])
    # for serializing the data returned from DB to UI
    @marshal_with(resource_fields)
    
    # GET req
    # just returning the videos
    def get(self, video_id):
        # abort_if_video_doesnt_exist(video_id)

        # query the database 
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video...")
        return result

    # PUT req
    # adding new videos
    @doc(description='Upload the video', tags=['Upload'])
    @marshal_with(resource_fields)
    def put(self, video_id):
        
        # abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()

        if result:
            abort(409, message="Video ID already exists..")
        
        #video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        video = VideoModel(id=video_id, name=rnames, views=0, likes=0)
        db.session.add(video)
        db.session.commit()
        return video, 201

    # for updating the fields
    # PATCH method
    @doc(description='Update video', tags=['Update video'])
    @marshal_with(resource_fields)
    def patch(self,video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video not found...")

        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']
        
        #db.session.add(result)
        db.session.commit()
        return result

    # DELETE req
    # delete the video
    @doc(description='Delete the video', tags=['Delete'])
    @marshal_with(resource_fields)
    def delete(self, video_id):
        # delete if the video exists
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video not found")
        video_to_delete = VideoModel.query.filter_by(id=video_id).delete()

        db.session.commit()
        return '', 204

# register the resource
api.add_resource(Video, "/video/<int:video_id>")
docs.register(Video)

# running the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT","5000"))
    app.run(host='0.0.0.0',port=port,debug=True)


