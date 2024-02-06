from flask import *
from fileinput import filename
# from distutils.log import debug
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/file_upload', methods = ['POST','GET'])
def file_upload():
    if request.method == 'POST':
        f = request.files.getlist('file')
        for file in f:
            file.save(file.filename)
        return '<h4> Files are uploaded Successfully </h4>'

if __name__ == '__main__':
    app.run(debug=True)