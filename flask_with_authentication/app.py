from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth
from models import People
from models import Activity

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

def verification(login, password):
    

class Peoples(Resource):
    def get(self, name):
        peoples = People.query.filter_by(name=name).first()
        try:
            response = {
                "name": peoples.name,
                "age": peoples.age,
                "id": peoples.id
            }
        except AttributeError:
            response = {
                "status": "Error",
                "Message": "person not found"
            }
        return response

    def put(self, name):
        peoples = People.query.filter_by(name=name).first()
        data = request.json

        if "name" in data:
            peoples.name = data["name"]
        if "age" in data:
            peoples.age = data["age"]
        peoples.save()

        response = {
            "id": peoples.id,
            "name": peoples.name,
            "age": peoples.age
        }

        return response

    def delete(self, name):
        peoples = People.query.filter_by(name=name).first()
        message = f"person {peoples.name} successfully deleted"
        peoples.delete()
        return {"status": "success",
                "message": message}


class LisPerson(Resource):
    def get(self):
        people = People.query.all()

        response = [{"id": i.id, "name": i.name, "age": i.age} for i in people]
        return response

    def post(self):
        data = request.json
        peoples = People(name=data["name"], age=data["age"])
        peoples.save()
        response = {
            "id": peoples.name,
            "name": peoples.name,
            "age": peoples.age
        }
        return response


class ListActivity(Resource):
    def get(self):
        activity = Activity.query.all()
        response = [{"id": i.id, "name": i.name, "peoples": i.peoples} for i in activity]

    def post(self):
        data = request.json
        peoples = People.query.filter_by(name=data["name"]).first()
        activity = Activity(name=data["name"], peoples=peoples)
        response = {
            "peoples": activity.peoples.name,
            "name": activity.name,
            "id": activity.id
        }
        return response


api.add_resource(Peoples, "/peoples/<string:name>/")
api.add_resource(LisPerson, "/peoples/")
api.add_resource(ListActivity, "/activity/")

if __name__ == '__main__':
    app.run(debug=True)
