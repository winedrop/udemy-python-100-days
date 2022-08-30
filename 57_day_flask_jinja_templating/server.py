from flask import Flask, render_template
import random
import datetime

import requests

app = Flask(__name__)


@app.route('/')
def home():
    #lets say that you want to generate a random number that will be used when the template is rendered
    random_number = random.randint(1,10)
    current_year = datetime.datetime.today().strftime("%Y")
    
    #when viewing the render_template definition you see **context, which is similar to **kwargs, can add as many keyword arguments as you want
    # need to have a keyword and value so that you can refer to it in the html 
    return render_template("index.html", num=random_number, curYear=current_year)

@app.route('/guess/<name_>')
def guess(name_):
    #run the name variable in agify and genderize
    genderize_endpoint = f"https://api.genderize.io?name={name_}"
    agify_endpoint = f"https://api.agify.io?name={name_}"
    request = requests.get(genderize_endpoint)
    print(request.content)
    gender_ = request.json()['gender']
    request = requests.get(agify_endpoint)
    print(request.content)
    age_ = request.json()['age']

    return render_template("guess.html", name=name_, gender=gender_, age=age_)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

