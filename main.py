"""Main program functions"""
from flask import Flask, render_template, session, redirect, url_for, escape, request
import requests
import content

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route("/")
@app.route("/planets/<page>")
def index_route(page="1"):
    api = "http://swapi.co/api/planets/?page=" + page
    data = requests.get(api).json()
    if 'username' in session:
        user = escape(session['username'])
        return render_template('planets.html', data=data, user=user)
    else:
        return render_template('planets.html', data=data)


@app.route("/login", methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        session['username'] = request.form['user']
        return redirect("/")
    mode = "Login"
    return render_template('login.html', mode=mode)


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect("/")


@app.route("/signup")
def signup_route():
    mode = "Register"
    return render_template('login.html', mode=mode)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()