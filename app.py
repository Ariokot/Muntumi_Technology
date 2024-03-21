import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

from mail import send_mail, EMAIL_ADDRESS, EMAIL_PASSWORD

# Configure application
app = Flask(__name__)
app.secret_key = 'sections2'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database

services_offered= ["UI/UX Design","Web Development", "Mobile App Development"]

@app.route("/")
def homepage ():
    return render_template("index.html", current_route="/")

@app.route("/work_withus", )  
def work_withus():
    print("work with us")
    return render_template("appointment.html",services_offered=services_offered) 

@app.route("/schedule_call", methods=["POST"])   
def schedule_call():
    recipient =request.form.get("email")
    send_mail(recipient)

    return redirect("/")
      

