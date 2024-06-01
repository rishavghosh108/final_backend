from flask import Blueprint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

_Send=Blueprint('send',__name__)

@_Send.route('/send',methods=['GET'])
def send():
    smtp_server = '52.23.17.251'
    smtp_port = 587
    sender_email = 'rishav@bengalintituteoftechnology.online'
    receiver_email = 'rishavghosh147@gmail.com'
    # sender_password = 'your_password'  # Use environment variables for better security

    subject = 'API Triggered Email'
    body = 'This email was sent because the API was accessed.'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        # server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return "Email sent successfully"
    except Exception as e:
        return f"Error: {e}"