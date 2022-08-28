from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

###NOTE To run the applicatio you can either use the flask command or python's -m switch with Flask
        #Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable
            #export FLASK_APP=hello.py
            #flask run
            # * Running on http://127.0.0.1:5000/

            #this stuff is run in the terminal

#effectively the flask framework is what determines which of these functions to call, only called when the decorator says it is appropriate to call them
@app.route('/')
def hello_world():
    return 'Hello, World!'

# can also just render html by returning the tag
#def hello_world():
#   return '<h1 style="text-align: center">Hello, World!</h1>' \
#           '<p>This is a paragraph.</p>' \ 
#           '<img src="some link here" width=200>'

@app.route("/bye")
def say_bye():
    return "Bye"

#@app.route("/username/<name>/1") || /username/AuCh/1 would have AuCh as the value of name
@app.route("/username/<path:name>/1") #/username/AuCh/1 would have AuCh/1 as the value of name
#could also do /username/<name>/<int:number> to specify the type of the variable
def greet(name):
    return f"Hello there {name}!"


#normally how you would run the server, in pycharm would allow you to use the run and stop buttons
if __name__ == "__main__":
    #without debug mode you would have to reload the server each time you make a change
    app.run(debug=True)

