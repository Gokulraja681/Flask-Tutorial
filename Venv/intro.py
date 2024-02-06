from flask import Flask, url_for, request, render_template, redirect
app = Flask(__name__)

#simple Flask Program
@app.route('/')
def index():
    return 'Hey my first webpage using Flask framework'

#simple dynamic flask program
@app.route('/dynamic/<person>')
def dynamic(person):
    return 'Hello %s!' %person

#simple flask program with html file
@app.route('/success/<name>')
def success(name):
    return 'Welcome %s !' %name

@app.route('/insert', methods = ['POST','GET']) 
def insert():
    if request.method == "POST":
        user = request.form.get('n')
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('n')
    return render_template("intro.html", )

if __name__ == ('__main__'):
    app.run(debug=True)