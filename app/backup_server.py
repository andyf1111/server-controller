from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)
app.secret_key = b'\x88\xec\x0eG2\xbf\xae~\xb0\x1f\xeb\xd3d2F\xf4'

users = {
    "a": "a"
}

def valid_login(name, password):
    return users.get(name) == password

def valid_session(ssid):
    return ssid is not None

@app.before_request
def before_request():
    ssid = request.cookies.get('ssid')
    if not valid_session(ssid) and request.endpoint != 'login':
        return redirect('login')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        ssid = request.cookies.get('ssid')
        if valid_session(ssid):
            return redirect('/')
        else:
            return render_template('login.html')
    else:
        if users.get(request.form['username']) == request.form['password']:
            resp = make_response(redirect('/'))
            resp.set_cookie('ssid', request.form['username'])
            return resp
        else:
            return redirect('login')
