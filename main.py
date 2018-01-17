from flask import Flask, request, render_template
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods = ['GET'])
def index():
    return render_template('signup.html')

@app.route("/", methods=['POST'])
def check_input():
    username = request.form['username']
    password = request.form['password_create']
    verify_password = request.form['password_verify']
    email = request.form['email']

    username_error= ""
    password_error= ""
    verify_error= ""
    email_error= ""

    if len(username) < 3 or len(username) > 20 or username.isalnum() == False:
        username_error = "Username must be between three and twenty alphanumeric characters."

    if len(password) < 3 or len(password) > 20:
        password_error = "Password must be between three and twenty alphanumeric characters."
        password = ""

    if verify_password == "" or verify_password != password:
        verify_error = "Both passwords must be identical."
        verify_password = ""

    if email != "":
        if "@" not in email or "." not in email:
            email_error = "Email needs @ and a period."

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template("confirmation.html", username = username)

    else:
        return render_template("signup.html", username_error = username_error, 
            password_error = password_error, verify_error = verify_error, email_error = email_error, 
            username = username, email = email)

if __name__== '__main__':
    app.run()