from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = b'\x88\xec\x0eG2\xbf\xae~\xb0\x1f\xeb\xd3d2F\xf4'

unintercept = ['login', 'static']
users = {"a": "a"}

def valid_session():
    re = 'username' in session
    return re

@app.before_request
def before_request():
    print(request.endpoint)
    if not valid_session() and request.endpoint not in unintercept:
        return redirect('login')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        if valid_session():
            return redirect("/")
        else:
            return render_template('login.html')
    else:
        if users.get(request.form['username']) == request.form['password']:
            session['username'] = request.form['username']
            return redirect('/')
        else:
            return redirect('login')
