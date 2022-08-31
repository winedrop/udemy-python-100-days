from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/about')
def about_page():
    return render_template("about.html")    

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

# @app.route('/blogs')
# def get_blog():
#     blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
#     response = requests.get(blog_url)
#     all_posts = response.json()
#     return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

    