import os
import smtplib

EMAIL_ADDRESS = os.environ.get('Email_User')
EMAIL_PASSWORD = os.environ.get('Email_password')


def send_mail(recipient):
    # access the mail server of the email provider and the port number
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()  
    

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = "Greetings!"
        body ="Hullo, World!"

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, recipient, msg)






