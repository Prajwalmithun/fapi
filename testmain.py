from flask import Flask
from flask_restful import Api, Resource


# initializing our app
app = Flask(__name__)

# wrap our app to api
api = Api(app)

# creating a resource
# create a class that inherits from "Resource" class.
# inside this we write API methods (overloading the methods and returning JSON data back)
class HelloWorld(Resource):
    # overloading the "get" method that is present in "Resource" class
    def get(self):
        # returing the data in form of JSON
        return {"data": "Hello World!"}

    # creating "POST" request
    # for testing : $ curl -X POST localhost:5000/helloworld
    def post(self):
        return {"data": "POST request is successfull!"}

names = {
    "prajwal" : {
        "name": "prajwal",
        "age": 23,
        "gender": "male"
    },

    "kushal": {
        "name": "kushal",
        "age": 20,
        "gender": "male"
    }
}

class Parameters(Resource):

    # GET request
    def get(self, name):
        # returing 2 values
        #return {"username": name, "age": age}

        # returning arrays
        return names[name] 


# registering the resource
# syntax = api.add_resource(<resource_name>, <endpoint>)
api.add_resource(HelloWorld, "/helloworld")
api.add_resource(Parameters, "/param/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)

