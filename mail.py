import os
import smtplib


EMAIL_ADDRESS = os.environ.get('Email_User')
EMAIL_PASSWORD = os.environ.get('Email_password')


def send_appointment_mail(recipient, name, service,date):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()  
    

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = "Your call has been scheduled"
        body = f"Hullo, {name}\n\nThank you for showing interest in working with Muntumi Technology. Your meeting call for {service} service on {date} has been set up. A member of our team will reach out to you with more details regarding the call. We look forward to working with you!\n\nMuntumi Technology"

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, recipient, msg)


def receive_email(sender,  sender_subject, sender_msg):
    # access the mail server of the email provider and the port number
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()  
    

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = f"Message from {sender}: {sender_subject}"
        body = sender_msg

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(sender, EMAIL_ADDRESS, msg)

def userMsg_reply(recipient):
    # access the mail server of the email provider and the port number
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()  
    

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = "We have received your message"
        body = f"We confirm receipt of your message, a technical member of our team with respond to you soon.\nThank you for contacting us.\n\nMuntumi Technology"

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, recipient, msg)        






