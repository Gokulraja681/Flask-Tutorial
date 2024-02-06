from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def home():
#     return '<center><h1>This is gokul raja webpage</h1></center>'

# @app.route('/hey')
# def hey():
#     return '<p> Hey are to interested in learning </p>'

# @app.route('/name/<user>/<int:age>')
# def name(user, age):
#     return f"My name is {user} and my age is {age}"

def index(username, age):
    return f"My name is {username} and my age is {age}"

app.add_url_rule('/username/<username>/<age>', 'index', index)


if __name__ == '__main__':
    app.run(debug=True)