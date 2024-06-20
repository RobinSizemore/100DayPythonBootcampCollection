from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper(**kwargs):
        output = "<b>"
        output += function(**kwargs)
        output += "</b>"
        return output
    return wrapper


@app.route("/username/<name>")
@make_bold
def greet(name):
    return (f"<h1 style='text-align: center'>Hello, {name}, how are you?</h1>"
            f"<p>This is a paragraph of text. I don't have Lorem Ipsum text, so I'm just going to keep "
            f"typing here.</p>")

if __name__ == "__main__":
    app.run(debug=True)
