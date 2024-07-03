from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Documentation about rendeing and flask
# https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates

"""
this run the app: `flask --app main run`

"""


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/hello/', methods=['GET'])
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/test', methods=['POST'])
def post_hello():
    print(time.time())
    print(request.method)
    print(request.data)
    return {}
    return render_template('hello.html', name=time.time())


if __name__ == "__main__":
    app.run(debug=True)
