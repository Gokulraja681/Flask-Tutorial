import pymongo
from flask import Flask, request, render_template, redirect, url_for


mongocon = pymongo.MongoClient('mongodb://localhost:27017')
mydb = mongocon['example']
mycol = mydb['sands']

app = Flask(__name__)

class User:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.mail = ""
        self.pswd = ""

gr = User()

@app.route('/create_account', methods=['POST', 'GET'])
def create_account():
    msg = None
    error = None
    if request.method == 'POST':
        gr.fname = request.form['fname']
        gr.lname = request.form['lname']
        gr.mail = request.form['mail']
        p = request.form['p']
        gr.pswd = request.form['pswd']
        
        if gr.pswd != p:
            msg = 'Passwords do not match'
        else:
            mydoc = {
            'fname' : gr.fname,
            'lname' : gr.lname,
            'mail' : gr.mail,
            'pswd' : gr.pswd
        }
            mycol.insert_one(mydoc)
            return redirect(url_for('profile'))
            
    return render_template('create_account.html', msg=msg, error=error)

@app.route('/profile', methods = ['POST', 'GET'])
def profile():
    details = mycol.find()
    return render_template('profile.html', details = details)

@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = None
    msg1 = None
    if request.method == 'POST':
        mail = request.form['mail']
        pswd = request.form['pswd']
        # Retrieve the document matching the provided email
        user = mycol.find_one({'mail': mail})
        if user and user['pswd'] == pswd:
            return redirect(url_for('Home'))
        else:
            msg1 = 'Mail or Password is not matched with each other'
    return render_template('login.html', msg=msg, msg1=msg1)


@app.route('/Home')
def Home():
    return '<html><body><h1> Login Pgae Successful </h1></body></html>'

@app.route('/')
def index():
    return render_template('E_index.html')

if __name__ == "__main__":
    app.run(debug=True)
