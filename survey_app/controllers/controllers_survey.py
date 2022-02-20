from survey_app import app
from flask import render_template, redirect, request, session
from survey_app.models.survey import Survey

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def form_results():
    if not Survey.validate_survey(request.form):
        return render_template('/retry.html', data = request.form)
    else:
        survey = {
            'fname': request.form['fname'],
            'lname': request.form['lname'],
            'location': request.form['location'],
            'language': request.form['language'],
            'comment': request.form['comment'],
        }
    Survey.save(survey)
    return render_template('result.html', survey = survey)

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')