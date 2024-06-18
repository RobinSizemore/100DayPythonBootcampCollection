from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<p><a href="/Hello">Hello</a>, World!</p><p>It\'s me, Robin!</p>'


@app.route('/Hello')
def hello_robin():
    return '<h3>Hello, Robin</h3>'


if __name__ == "__main__":
    app.run()
