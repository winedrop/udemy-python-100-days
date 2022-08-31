from flask import Flask, render_template, request
import requests

app = Flask(__name__)
blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()
@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/about')
def about_page():
    return render_template("about.html")    

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        return render_template("contact.html", messageStatus=True)
        pass
    else:
        return render_template("contact.html")

@app.route('/blog/<num>')
def get_blog(num):
    return render_template("post.html", post=all_posts[int(num)])

if __name__ == "__main__":
    app.run(debug=True)

    