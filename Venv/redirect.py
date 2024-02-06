from flask import Flask, redirect, url_for, request
app = Flask(__name__)

# @app.route('/')
# def index():
#     return redirect('/test2')

# @app.route('/test')
# def test():
#     return 'Gokul Raja Re-directed Page'

# @app.route('/test2')
# def test2():
#     return 'Gokul Re-directed page attempt-2'

@app.route('/admin')
def gokul():
    return '<h1> Hello Admin ! </h1>'

@app.route('/guest/<name>')
def hello_guest(name):
    return f'<h1> Hello {name} you as guest ! </h1>'

@app.route('/main/user')
def main(user):
    if user == 'admin':
        return redirect(url_for('gokul'))
    else:
        return redirect(url_for('hello_guest', name = user))
    

if __name__ == ('__main__'):
    app.run(debug=True)