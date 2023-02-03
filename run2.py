from flask import Flask

app = Flask(__name__)


# With the POST method I can access it in Postman
@app.route("/", methods=["POST"])
def hello():
    return "Hello World"


if __name__ == "__main__":
    app.run()
