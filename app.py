from flask import Flask, flash, render_template, request, redirect,  url_for
from wtforms import Form, FileField
from werkzeug import secure_filename
import os
from fastai.vision import *

app = Flask(__name__)
learner = load_learner('/home/vinay/HFC/models')
# Often people will also separate these into a separate config.py file 
app.config['SECRET_KEY'] = 'NOTAKEY'
app.config['UPLOAD_FOLDER'] = '/home/vinay/HFC/static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Views for pages
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

    test_img = open_image(filepath)
    pred_class, pred_id, outputs = learner.predict(test_img)
    img_url = url_for('static', filename='images/'+filename)
    return render_template('result.html', pred_class = str(pred_class), image = img_url)

if __name__ == '__main__':
    app.run(debug=True)
    