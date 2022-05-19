from flask import Flask, make_response, render_template, request
from flask_bootstrap import Bootstrap
from .form import Form
import logging
import sys
from .mailer import send_mail
from .analyzer import analyze
from .utils import generate_html_report

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ZXTxCzStTCTCW3alyFPqYICesaCPOEO6'
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
Bootstrap(app)


@app.route('/api/v1/analyze', methods=['POST'])
def api_analyze():
    try:
        text = request.form['text']
        text = text.strip()
        text = text.replace('\r', '')
        text = text.replace('\n', '')
        text = text.replace('\t', '')
        text = " ".join(text.split())
        result = analyze(text)
        return make_response(result, 200)
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/', methods=['GET', 'POST'])
def index():
    message = 'You will receive an email with the results.'
    form = Form()
    if form.validate_on_submit():
        # filename = secure_filename(form.text_file.data.filename)
        email = form.email.data
        # Do something with the form data
        text = form.text_file.data.read().decode('utf-8').strip()
        text = text.replace('\r', '')
        text = text.replace('\n', ' ')
        text = text.replace('\t', '')
        text = " ".join(text.split())
        result = analyze(text)
        # Send email after successful form submission
        html = generate_html_report(result['verbs'], result['nouns'],result['text'])
        send_mail(to=[{"Email": email}], subject='Text Analysis Results', text='Text Analysis Results', html=html)
        return render_template('form.html', form=form, message=message)
    else:
        if form.errors:
            print(form.errors)
            message = form.errors['text_file'][0]
            return render_template('form.html', form=form, message=message)
        return render_template('form.html', form=form, message='')
