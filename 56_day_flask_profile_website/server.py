from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
#if your html has static files like an image or css, it would need to go in the static folder and would probably need to edit the file path

#chrome likes to cache static files when loading the website so things like edits to background color will not change without a hard reload
# hard reload on chrome is holding shift and clicking the refresh button

if __name__ == "__main__":
    app.run(debug=True)

#nice way of editing html from the browser is to go to the console and input the command:
## document.body.contentEditable=true
## now you can click on elements on the page and start to edit them
## to delete elements, you just select them like normal and delete the html
### to keep the changes you need to save the page/html from the page 