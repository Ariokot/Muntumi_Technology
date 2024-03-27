import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

from mail import send_appointment_mail, receive_email, EMAIL_ADDRESS, EMAIL_PASSWORD

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
    name = request.form.get("first_name")
    service = request.form.get("service")
    date = request.form.get("date")
    send_appointment_mail(recipient, name, service, date)

    schedulled_call = True

    return render_template("flashmsg.html", current_route="schedulled_call")

@app.route("/user_msg", methods=["POST"])  
def user_msg():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    msg = request.form.get("msg")
    receive_email(email, subject, msg)
    
    return render_template("flashmsg.html", current_route="user_msg")

@app.route("/admin_reg", methods=["GET"])    
def admin_reg():
    return render_template("admin_reg.html", current_route="admin_reg")

@app.route("/admin_signin",  methods=["GET", "POST"])  
def admin_signin():
    if request.method == "GET":
        return render_template("admin_signin.html", current_route="admin_signin")  


      

