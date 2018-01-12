from flask import Flask, request, render_template
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods = ['GET'])
def index():
    return render_template('Signup.html')

@app.route("/registration", methods=['POST'])
def check_input():
    username=request.form['username']
    if len(username) < 3 or len(username) > 20 or username.isalnum() == False:
        return render_template('Signup.html',username = 'username must be between three and twenty characters(letters and numbers)')

    password = request.form['password_create']
    p1 = request.form['password_create']
    p2 = request.form['password_verify']
    if len(p1) <3 or len(p1) >20:
        return render_template('Signup.html', password = 'password must be 3 to 20 charactors', k = username)
    if p1 == p2:
        template = jinja_env.get_template('confirmation.html')
        return template.render(username = username)
    else:
        return render_template('Signup.html', password = 'passwords must match', k = username)

    email=request.form['email']
    if len(email) < 3 or len(email) > 20:
        return render_template('Signup.html',
        email = 'Must be between 3 to 20 characters long, including the domain name', k = username, e = email)

    at_dot = 0
    for char in email:
        if char =='@' or char == '.':
            at_dot += 1
    if at_dot !=2:
        return render_template('Signup.html', email = 'Invalid Email.', k = username, e = email)

if __name__== '__main__':
    app.run()