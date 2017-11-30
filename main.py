from flask import Flask, request, redirect, render_template
import cgi
import os



app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('signup.html')

@app.route('/signup')
def display_signup_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def validate_info():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

#ERROR TRIGGERS
#---------------
##user leaves any of the following fields empty: username, password, verify password.
###user's username or password is not valid -- contains a space character or < 3 chars or > 20 chars
    if (username == '' or (len(username) < 3 or len(username) >20) or (" " in username)):
        username_error = "That's not a valid username, try again."
        username = ''
    if (password == '' or (len(password) < 3 or len(password) >20) or (" " in password)):
        password_error = "That's not a valid password, try again."
        password = ''
#The user's password and password-confirmation do not match.
    if verify_password == '' or verify_password != password:
        verify_password_error = "Passwords don't match."
        verify_password = ''
#Email field may be left empty, but if there is content in it, then it must be validated
    if email != '':
    #valid email address must contain a single @, a single ., contains no spaces, and is between 3 and 20 characters long
        if ('@' not in email or '.' not in email or ' ' in email or (len(email) < 3 or len(email) >20)):
            email_error = "That's not a valid email."
            email = ''


    if not username_error and not password_error and not verify_password_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
    #If user's form submission is not valid, you should reject it and re-render the form with some feedback to inform the user of what they did wrong
        return render_template('signup.html',
        username_error = username_error,
        password_error = password_error,
        verify_password_error = verify_password_error,
        email_error = email_error,
        username = username,
        password = password,
        verify_password = verify_password,
        email = email)

# Valid Input: show the user a welcome page that uses the username input to display a welcome message of: "Welcome, [username]!"
@app.route('/welcome')
def valid_entry():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()
