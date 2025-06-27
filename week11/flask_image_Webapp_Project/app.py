import os
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    img_url = None
    if request.method == 'POST':
        file = request.files['image']
        if file and file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            img_url = url_for('static', filename='uploads/' + file.filename)
    return render_template('index.html', img_url=img_url)
if __name__ == '__main__':
    app.run(debug=True)
