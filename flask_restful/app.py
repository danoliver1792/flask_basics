from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
import json

app = Flask(__name__)
api = Api(app)

developers = [
    {
        "id": "0",
        "name": "Danrlei",
        "skills": ["Python", "Flask"]
    },
    {
        "id": 1,
        "name": "Andressa",
        "skills": ["Python", "Django"]
    }
]


class Developer(Resource):
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            message = f"developer {id} does not exist"
            response = {"status": "error",
                        "message": message}
        except Exception:
            message = "unknown error"
            response = {"status": "error",
                        "message": message}
        return response

    def put(self, id):
        datas = json.loads(request.data)
        developers[id] = datas
        return datas

    def delete(self, id):
        developers.pop(id)
        return {"status": "success",
                "message": "record deleted"}


class DevelopersList(Resource):
    def get(self):
        return developers

    def post(self):
        datas = json.loads(request.data)
        position = len(developers)
        datas["id"] = position
        developers.append(datas)
        return developers[position]


api.add_resource(Developer, "/dev/<int:id>/")
api.add_resource(DevelopersList, "/dev/")

if __name__ == "__main__":
    app.run(debug=True)
