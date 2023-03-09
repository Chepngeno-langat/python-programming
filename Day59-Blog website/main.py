from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/c6b2f43138db0fa15965").json()

app = Flask(__name__)
@app.route("/")
def home_page():
    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

if __name__ == '__main__':
   app.run(debug=True)