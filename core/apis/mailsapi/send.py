from flask import Blueprint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

_Send=Blueprint('send',__name__)

@_Send.route('/send',methods=['GET'])
def send():
    smtp_server = "52.23.17.251"  # IP address of your SMTP server
    smtp_port = 1025  # Port where your custom SMTP server is running
    sender_email = 'rishav@bengalintituteoftechnology.online'
    receiver_email = 'rishavghosh147@gmail.com'
    sender_password = 'your_password'  # Use environment variables for better security

    subject = 'API Triggered Email'
    body = 'This email was sent because the API was accessed.'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        print(f"Connecting to SMTP server {smtp_server} on port {smtp_port}")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.set_debuglevel(1)  # Enable debug output
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return "Email sent successfully"
    except Exception as e:
        return f"Error: {e}"