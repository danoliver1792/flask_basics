from flask import Flask
from flask import jsonify
from flask import request
import json

# adding values with Postaman's Body and Raw
app = Flask(__name__)


@app.route("/<int:id>")
def people(id_name):
    return jsonify({"id_name": id_name,
                    "name": "Danrlei",
                    "profession": "developer"})


# @app.route("/sum_values/<int:value1>/<int:value2>/")
# def sum_values(value1, value2):
#    return jsonify({"sum": value1 + value2})

@app.route("/sum_values", methods=["POST"])
def sum_values():
    datas = json.loads(request.data)
    total = sum(datas["values"])
    return jsonify({"sum_values": total})


if __name__ == "__main__":
    app.run(debug=True)
