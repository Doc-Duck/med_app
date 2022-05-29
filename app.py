from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import random
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = 'static/files'
app.config["TEMPLATES_AUTO_RELOAD"] = True


class UploadFile(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Upload file')


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    xy = [51, 50, 150, 100]
    form = UploadFile()
    percent = random.randint(60, 90)
    pos = [xy[0], xy[1], xy[2]-xy[0], xy[3]-xy[1]]
    if form.validate_on_submit():
        file = form.file.data
        res = os.path.join('static/files/', secure_filename(file.filename))
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return render_template('index.html', form=form, pos=pos, percent=percent, file=res)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
