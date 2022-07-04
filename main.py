from flask import Flask, render_template
import requests

app = Flask(__name__)

posts_endpoint = "https://api.npoint.io/f74d23408742b9aea05a"
all_posts = requests.get(posts_endpoint).json()

@app.route("/")
def get_home():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")