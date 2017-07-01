"""Main program functions"""
from flask import Flask, render_template
import requests
import content

app = Flask(__name__)


@app.route("/")
@app.route("/planets/<page>")
def index_route(page="1"):
    api = "http://swapi.co/api/planets/?page=" + page
    data = requests.get(api).json()
    return render_template('planets.html', data=data)


@app.route("/login")
def login_route():
    mode = "Login"
    return render_template('login.html', mode=mode)


@app.route("/signup")
def signup_route():
    mode = "Register"
    return render_template('login.html', mode=mode)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()