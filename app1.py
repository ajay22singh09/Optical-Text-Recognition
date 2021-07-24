import os
from flask import Flask, render_template, request, redirect, url_for 
# import our OCR function
from ocr_core import ocr_core

app=Flask(__name__,template_folder='templates')
UPLOAD_FOLDER = '.'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'pdf'])
#ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# route and function to handle the home page
@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/upload', methods = ['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            # call the OCR function on it
            extracted_text = ocr_core(file)

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run()
