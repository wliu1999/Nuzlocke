# Flask imports
import flask
import requests
from flask import Flask, redirect, request
from flask import render_template
from flask import session
from flask import abort

# Login Tools
from flask_login import LoginManager
from flask_login import UserMixin
from flask_login import login_required
from flask_login import login_user
from flask_login import current_user

# Database Imports
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pokedata")
def pokedata():
    return render_template("pokedata.html")


app.run()
