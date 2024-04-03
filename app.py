import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

from mail import send_appointment_mail, receive_email, userMsg_reply, EMAIL_ADDRESS, EMAIL_PASSWORD

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
db = SQL("sqlite:///admin.db")

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
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    organisation = request.form.get("organisation")
    service = request.form.get("service")
    date = request.form.get("date")
    send_appointment_mail(recipient, first_name, service, date)

    #Insert data to database
    db.execute("INSERT INTO user_appointments (first_name, last_name, organisation, email,service, date) VALUES (?,?,?,?,?,?)", first_name, last_name, organisation, recipient, service, date)

    schedulled_call = True

    return render_template("flashmsg.html", current_route="schedulled_call")

@app.route("/user_msg", methods=["POST"])  
def user_msg():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    msg = request.form.get("msg")

    #Insert data to database
    db.execute("INSERT INTO user_msgs(name, email, subject, message) VALUES (?,?,?,?)", name, email, subject, msg)

    #User sends message to us
    receive_email(email, subject, msg)

    #User recieves auto response confirmaing receipt
    userMsg_reply(email)
    
    return render_template("flashmsg.html", current_route="user_msg")

@app.route("/admin_reg", methods=["GET", "POST"])    
def admin_reg():
    if request.method == "GET":
        return render_template("admin_reg.html")
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        password1 = request.form.get("password")
        password2= request.form.get("verify-password")

        if password1 == password2:
            password_verified = True
            print("password verified")  
            password = password1      

            #Add admin user to database
            db.execute("INSERT INTO admin_users(name, email, password) VALUES (?,?,?)", name, email, password)   

            return render_template("admin_signin.html")
        
        else:
            password_not_verified = True  
            msg = "Passwords not match.Try again"              
            return render_template("admin_reg.html", msg=msg, name=name,email=email)


@app.route("/admin_signin",  methods=["GET", "POST"])  
def admin_signin():
    if request.method == "GET":
        return render_template("admin_signin.html")  

    else:
        email = request.form.get("admin_name")
        print(email)
        password = request.form.get("admin_pwd")
        print(password)

        confirm_user = db.execute("SELECT * FROM admin_users WHERE email = ? AND password = ?", email, password)
        print(confirm_user)
        if confirm_user:
            return render_template("admin_loggedin.html", current_route="admin_loggedin")
        else:
            msg = "Email or Password is incorrect. Try again"
            return render_template("admin_signin.html", msg=msg)    


    



@app.route("/admin_loggedin", methods=["GET"])       
def admin_loggedin():
    return render_template("admin_loggedin.html", current_route="admin_loggedin") 

@app.route("/user_appointments")    
def user_appointments():

    user_appointments_info = db.execute("SELECT * FROM user_appointments")
    print(user_appointments_info)

    #for i in range(len(user_appointments_info)):
    #    dict_items = list(user_appointments_info[i].items())
    #    user_appointments_info[i] = dict(dict_items[1:])
    #print(user_appointments_info)

    my_list = []
    for dictionary in user_appointments_info:
        my_dict = {}
        my_dict["id"] = dictionary["id"]
        my_dict["name"] = dictionary["first_name"] + " " + dictionary["last_name"]
        my_dict["organisation"] = dictionary["organisation"] 
        my_dict["email"] = dictionary["email"] 
        my_dict["service"] = dictionary["service"]
        my_dict["date"] = dictionary["date"]  
        my_list.append(my_dict)
        
    print(my_list)    


    keys_list = []
    if my_list:
        for key in my_list[0].keys():
            #print(key)
            if "_" in key:
                new_key = key.replace("_", " ").title()
            elif key == "id":
                new_key = "User No."    
            else:
                new_key = key.title()
            keys_list.append(new_key)    
            #print(new_key)  

    print(keys_list)          
   
    return render_template("admin_loggedin.html", current_route="user_appointments", my_list=my_list, keys_list=keys_list) 

@app.route("/user_msgs")
def user_msgs():
    userMsg_info = db.execute("SELECT * FROM user_msgs")
    print(userMsg_info)

    keys_list = []
    if userMsg_info:
        for key in userMsg_info[0].keys():
            #print(key)
            if "_" in key:
                new_key = key.replace("_", " ").title()
            elif key == "id":
                new_key = " No."    
            else:
                new_key = key.title()
            keys_list.append(new_key)    
            #print(new_key)  

    print(keys_list)          

    return render_template("admin_loggedin.html", current_route="user_msgs", keys_list=keys_list, userMsg_info=userMsg_info) 

@app.route("/admin_logout", methods=["GET"]) 
def admin_logout():
    return redirect("/admin_signin")
         



      

