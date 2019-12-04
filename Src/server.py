import os
from flask import Flask, render_template, request, redirect,url_for
from main import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_data',methods=['POST'])
def handle_data():
    defF = request.files['defF']
    defF.save(os.path.join('D:/Uni/Fall 19/DD2/DEFTOSVG-master/Source code', defF.filename))


    lefF = request.files['lefF']
    lefF.save(os.path.join('D:/Uni/Fall 19/DD2/DEFTOSVG-master/Source code', lefF.filename))

    DEF = defF.filename
    LEF = lefF.filename

    SVG = toSVG(DEF,LEF)
    return render_template(SVG)

if __name__ == '__main__':
    app.run(debug=True)