from flask import Flask, render_template, redirect, url_for
import random
import datetime
import requests


app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.today().year
    text = "Hello, World!"
    kwargs = {"rand_num": random_number, "current_year": current_year, "text": text}
    return render_template("index.html", **kwargs)


@app.route('/guess/<name>')
def name_page(name):
    params = {"name": name}
    age_resp = requests.get(url="https://api.agify.io", params=params)
    params["age"] = age_resp.json()["age"]

    gender_resp = requests.get(url="https://api.genderize.io", params=params)
    params["gender"] = gender_resp.json()["gender"]

    return render_template("name.html", **params)


@app.route('/blog')
def blog_redirect():
    return redirect(url_for('blog_page', num=0))


@app.route('/blog/<num>')
def blog_page(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("blog-main.html", posts=all_posts, post_id=int(num))


if __name__ == "__main__":
    app.run(debug=True)
