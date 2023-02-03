from flask import Flask
from flask import jsonify
from flask import request
import json

# using other methods
app = Flask(__name__)


@app.route("/<int:id>")
def people(id_name):
    return jsonify({"id_name": id_name,
                    "name": "Danrlei",
                    "profession": "developer"})


# @app.route("/sum_values/<int:value1>/<int:value2>/")
# def sum_values(value1, value2):
#    return jsonify({"sum": value1 + value2})

@app.route("/sum_values", methods=["POST", "GET"])
def sum_values():
    if request.method == "POST":
        datas = json.loads(request.data)
        total = sum(datas["values"])
    elif request.method == "GET":
        total = 10 + 10
    return jsonify({"sum_values": total})


if __name__ == "__main__":
    app.run(debug=True)
