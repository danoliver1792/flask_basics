from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

developers = [
    {"name": "Danrlei",
     "skills": ["Python",
                "Flask"]
     },
    {"name": "Andressa",
     "skills": ["Python",
                "Django"]}
]


# returns a developer by ID, change and delete
@app.route("/dev/<int:id>/", methods=["GET", "PUT", "DELETE"])
def developer(id):
    if request.method == "GET":
        try:
            response = developers[id]
        except IndexError:
            message = f"id developer {id} does not exist"
            response = {"status": "Error",
                        "message": message}

        except Exception:
            message = "unknown error"
            response = {"status": "Error",
                        "message": message}

        return jsonify(response)

    elif request.method == "PUT":
        datas = json.loads(request.data)
        developers[id] = datas
        return jsonify(datas)

    elif request.method == "DELETE":
        developers.pop(id)
        return jsonify({"status": "success",
                        "message": "record deleted"})


# entering data and listing all, allows to register
@app.route("/dev/", methods=["POST", "GET"])
def list_developers():
    if request.method == "POST":
        datas = json.loads(request.data)
        developers.append(datas)
        return jsonify({"status": "success",
                        "message": "inserted record"})


if __name__ == "__main__":
    app.run(debug=True)
