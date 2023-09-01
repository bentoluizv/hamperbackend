from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World {name}!</p>".format(name=__name__)

if __name__ == "__main__":
    app.run(debug=True)