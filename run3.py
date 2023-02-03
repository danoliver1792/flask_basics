from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    return "Hello World."


# With debug, it restarts automatically
if __name__ == "__main__":
    app.run(debug=True)
