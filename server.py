from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ALL 4 one, 1 for all."

@app.route('/')
def index():
    if 'isNewForm' in session:
        pass
    else:
        session['isNewForm'] = True
    print(session)
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def form_results():
    for key in request.form:
        print(key)
        session[key] = request.form[key]
        print(session[key])
    
    print(session)
    return render_template('result.html')

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
