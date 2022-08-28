from flask import Flask
app = Flask(__name__)


###NOTE To run the applicatio you can either use the flask command or python's -m switch with Flask
        #Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable
            #export FLASK_APP=hello.py
            #flask run
            # * Running on http://127.0.0.1:5000/

            #this stuff is run in the terminal

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)

#normally how you would run the server, in pycharm would allow you to use the run and stop buttons
if __name__ == "__main__":
    #without debug mode you would have to reload the server each time you make a change
    app.run(debug=True)