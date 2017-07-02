"""Main program functions"""
from flask import Flask, render_template, session, redirect, escape, request, json
from werkzeug.security import check_password_hash, generate_password_hash
import requests
import re
import content
import users

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route("/")
@app.route("/planets/<page>")
def index_route(page="1"):
    page = "1" if int(page) < 1 else page
    api = "http://swapi.co/api/planets/?page=" + page
    data = requests.get(api).json()
    user = ""
    if 'username' in session:
        user = escape(session['username'])
    return render_template('planets.html', data=data, user=user)


@app.route("/login", methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        pwhash = users.get_psw(request.form['user'])
        if check_password_hash(pwhash, request.form['psw']):
            session['username'] = request.form['user']
            return redirect("/")
    mode = "Login"
    return render_template('login.html', mode=mode)


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect("/")


@app.route("/signup", methods=['GET', 'POST'])
def signup_route():
    if request.method == 'POST':
        psw = generate_password_hash(request.form['psw'])
        users.register_new(request.form['user'], psw)
        mode = "Login"
    else:
        mode = "Register"
    return render_template('login.html', mode=mode)


@app.route('/vote', methods=['POST'])
def vote_route():
    data = requests.get(request.json['url']).json()
    planet_id = int(re.findall(r'\d+', request.json['url'])[0])
    user = escape(session['username'])
    users.handle_vote(data['name'], planet_id, user)
    return json.dumps({'status': 'OK', 'planet': data['name']})


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
