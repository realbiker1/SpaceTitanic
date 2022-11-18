from app import app
from flask import render_template, session, redirect, url_for, request
import pickle

from app.forms import DataForm
from app.predict import preprocess, predict, postprocess


app.config['SECRET_KEY'] = 'DAT158'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():

    form = DataForm()
    if form.validate_on_submit():

        for fieldname, value in form.data.items():
            session[fieldname] = value

        user_info = request.headers.get('User-Agent')

        data = preprocess(session)

        pred = predict(data)

        pred = postprocess(pred)

        session['user_info'] = user_info
        session['pred'] = pred


        return redirect(url_for('index'))

    return render_template('index.html', form=form)



@app.route('/dashboard')

def dashboard():
    return render_template('dashboard.html')