# # Flask GET method Example
# from flask import Flask, request, render_template
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1> Using the HTTP methods in the Flask Framework </h1>'

# @app.route('/square', methods=['GET'])
# def square():
#     if request.method == 'GET':
#         if request.args.get('num') is None:
#             return render_template('square.html')
#         elif request.args.get('num') == '':
#             return '<html> <body> Enter Number is Invalid </body> </html>'
#         else:
#             number = request.args.get('num')
#             sq = int(number) ** int(number)
#             return render_template('answer.html', sq=sq, num=number)

# if __name__ == '__main__':
#     app.run(debug=True)


#POST Method in Flask
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'This my flask web page using the post method in flask framework'

@app.route('/square', methods = ['POST', 'GET'])
def square():
    if request.method == 'POST':
        if (request.form['num'] == ''):
            return '<html><body> Invalid Format </body></html>'
        else:
            number = request.form.get('num')
            sq = int(number) * int(number)
            return render_template('answer.html', sq = sq)
        
    if request.method == 'GET':
        return render_template('square.html')

if __name__ == '__main__':
    app.run(debug=True)