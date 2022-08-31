from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

#methods parameter receives a dictionary, so you can have multiple methods targeted by one route
@app.route("/login", methods=["POST"])
def receive_data():
    #do something
    if request.method == 'POST':
        request.form['username']
        request.form['password']
    return render_template('login.html', uname=request.form['username'], pword=request.form['password'])
    pass

# # example of multiple methods
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)


