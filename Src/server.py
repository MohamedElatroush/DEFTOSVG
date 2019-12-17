import os
from flask import Flask, render_template, request, redirect,url_for
from main import *
from werkzeug.utils import secure_filename


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_data',methods=['POST'])
def handle_data():
    defF = request.files['defF']
    defF.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(defF.filename)))
    lefF = request.files['lefF']
    lefF.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(lefF.filename)))
    drcfF = request.files['drcfF']
    drcfF.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(drcfF.filename)))

    DEF = defF.filename
    LEF = lefF.filename
    DRC = drcfF.filename

    SVG = toSVG(DEF, LEF, DRC)
    return render_template(SVG)

if __name__ == '__main__':
    app.run(debug=True)
