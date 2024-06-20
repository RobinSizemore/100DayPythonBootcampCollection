from flask import Flask
from functools import wraps
import random

app = Flask(__name__)

random_number = -1
OUT_OF_BOUNDS = "https://giphy.com/gifs/abcnetwork-abc-blackish-black-ish-hv9cgiPymNxlk7F8jo"
GUESS = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDg2YXF2Mndnb3Q3NWdnY2NkaG1zMGxlNTczYmYya2Z6cG96aHBoYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hTrCbhPoQEcCT18JLf/giphy.webp"
TOO_LOW = "https://media4.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/200.webp?cid=790b7611mwhdfhmd9qvk45f29fjm1zpoewj1n0rb4etnc569&ep=v1_gifs_search&rid=200.webp&ct=g"
TOO_HIGH = "https://media4.giphy.com/media/3og0IuWMpDm2PdTL8s/200.webp?cid=790b7611ksvtbmc76qu2u5sl6ffbfk9db6mxpt2dzr3znebm&ep=v1_gifs_search&rid=200.webp&ct=g"
JUST_RIGHT = "https://media3.giphy.com/media/mWNZzjb63tFEY0Ze2j/giphy.webp?cid=790b761168g4o54lhuoj9vrsypa9rgqjt5az2yzwft9e4qes&ep=v1_gifs_search&rid=giphy.webp&ct=g"

def guesser(function):
    @wraps(function)
    def wrapper(**kwargs):
        output = function(**kwargs)
        output += "<p>Guess "
        for i in range(10):
            output += f"<a href='/{i}'>{i}</a> | "
        output += "<a href='/'>RESTART</a></p>"
        return output
    return wrapper


@app.route("/")
@guesser
def start():
    global random_number
    random_number = random.randint(0, 9)
    output = "<h1 style='text-align: center'>Guess a number</h1>"
    output += "<p>I have selected a number between 0 and 9 (inclusive).  Try to guess what it is</p>"
    output += ("<span style='text-align: center'><img "
               f"src='{GUESS}' /></span>")
    return output


@app.route("/<number>")
@guesser
def number_guess(number):
    number = int(number)
    global random_number
    output = ""
    if number < 0 or number > 9:
        print(f"{number} out of range")
        output = "<h1 style='text-align: center'>OUT OF RANGE!</h1>"
        output += "<p></p>"
        output += f"<img src='{OUT_OF_BOUNDS}' />"
    elif number < random_number:
        print(f"{number} < {random_number}")
        output = "<h1 style='text-align: center'>TOO LOW!</h1>"
        output += "<p></p>"
        output += f"<img src='{TOO_LOW}' />"
    elif number > random_number:
        print(f"{number} > {random_number}")
        output = "<h1 style='text-align: center'>TOO HIGH!</h1>"
        output += "<p></p>"
        output += f"<img src='{TOO_HIGH}' />"
    else:
        print(f"{number} == {random_number}")
        output = "<h1 style='text-align: center'>GOT IT!</h1>"
        output += "<p></p>"
        output += f"<img src='{JUST_RIGHT}' />"
    print(output)
    return output

if __name__ == "__main__":
    app.run(debug=True)


