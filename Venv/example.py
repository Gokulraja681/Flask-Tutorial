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
    msg1 = None
    msg2 = None
    error = None
    if request.method == 'POST':
        gr.fname = request.form['fname']
        gr.lname = request.form['lname']
        temp_mail = request.form['mail']
        
        if mycol.find_one({'mail': temp_mail}):
            msg1 = 'Email already exists'
        else:
            p = request.form['p']
            if len(p) < 8:
                msg2 = 'Password must contain 8 characters'
            else:
                gr.mail = temp_mail
                gr.pswd = request.form['pswd']
                if gr.pswd != p:
                    msg = 'Passwords do not match'
                if (len(p) > 8) and (gr.pswd == p):
                    mydoc = {
                        'fname': gr.fname,
                        'lname': gr.lname,
                        'mail': gr.mail,
                        'pswd': gr.pswd
                    }
                    mycol.insert_one(mydoc)
                    return redirect(url_for('profile'))
            
    return render_template('create_account.html', msg=msg, msg1=msg1, msg2=msg2, error=error)


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
        user = mycol.find_one({'mail': mail})
        if user and user['pswd'] == pswd:
            return redirect(url_for('Home'))
        else:
            msg1 = 'Mail or Password is not matched with each other'
    return render_template('login.html', msg=msg, msg1=msg1)

@app.route('/delete', methods = ['POST', 'GET'])
def delete():
    if request.method == 'POST':
        mail = request.form['mail']
        pswd = request.form['pswd']
        user = mycol.find_one({'mail': mail})
        if user and user['pswd'] == pswd:
            mycol.delete_one(user)
            return 'Account deleted succesfully'
        else:
            return 'Account not exists '
    return render_template('delete.html') 

@app.route('/forget_password', methods = ['POST', 'GET'])
def forget_password():
    if request.method == 'POST':
        mail = request.form['mail']
        temp_pswd = request.form['temp_pswd']
        user = mycol.find_one({'mail': mail})
        if user: 
            mycol.update_one({'mail': mail},{'$set':{'pswd': temp_pswd}})
            return redirect(url_for('profile'))
        else:
            return 'mail not exists'
    return render_template('forget_password.html')

@app.route('/Home')
def Home():
    return '<html><body><h1> Login Page Successful </h1></body></html>'

@app.route('/')
def index():
    return render_template('E_index.html')

if __name__ == "__main__":
    app.run(debug=True)
