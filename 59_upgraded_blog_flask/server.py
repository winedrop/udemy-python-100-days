from flask import Flask, render_template, request
import requests
import smtplib

OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"

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
        send_email(request.form['fullname'], request.form['user-email'], request.form['user-phone-number'], request.form['user-message'])
        return render_template("contact.html", messageStatus=True, )
        pass
    else:
        return render_template("contact.html")

@app.route('/blog/<num>')
def get_blog(num):
    return render_template("post.html", post=all_posts[int(num)])

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True)

    