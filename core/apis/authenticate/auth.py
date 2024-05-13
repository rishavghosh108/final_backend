from werkzeug.security import generate_password_hash
from datetime import datetime,timedelta
import jwt,os,random,vonage
from core.libs.assertions import assert_found,assert_valid
from twilio.rest import Client

def GenPasswordHash(password):
    return generate_password_hash(password)

def Gen(payload, secret_key):
    return jwt.encode(payload, secret_key, algorithm='HS256')

def SetTime(time):
    time=datetime.now()+timedelta(minutes=time)
    return int(time.timestamp())

def TransformData(data):
    dob_str = data['user']['dob'].isoformat()
    return {
        "user": {
            "name": data['user']['name'].lower(),
            "gender": data['user']['gender'].lower(),
            "dob": dob_str,
            "mobile": data['user']['mobile']
        },
        "username": {
            "email": data['username']['email'].lower(),
            "password": GenPasswordHash(data['username']['password'])
        }
    }

def GenToken(data, type, no):
    exp_time=SetTime(15)
    payload={"data":data, "type":type, "expire": exp_time}
    return Gen(payload, str(GenOtp(no)))

def Decript(token, secret_key):
    try:
        payload=jwt.decode(token, str(secret_key['otp']),algorithms=['HS256'])
    except:
        assert_found(None,'please enter correct otp')
    assert_valid(payload['expire']>int(datetime.now().timestamp()),"otp has been expired !!!")
    return payload

def Authorization(email):   #used for login
    # send_email()
    exp_time=SetTime(60)
    payload={"email":email,"expire":exp_time}
    return Gen(payload,os.getenv('authorization_secret_key'))

def Decrept_email(token):
    try:
        payload=jwt.decode(token,os.getenv('authorization_secret_key'),algorithms=['HS256'])
    except:
        assert_found(None,"Don't do this anymore")
    assert_valid(payload['expire']>int(datetime.now().timestamp()),"token has been expired !!!")
    return payload['email']

def GenOtp(no):
    otp=random.randint(1000,9999)
    SendOtp("+91"+f"{no}", otp)
    return otp

def SendOtp(no,otp):

    try:
        client = Client('AC99a3cb7bcba53d412b83b47cf49aa9bd', '1405c57861ea2aa00bd81eeec3e0d2e1')

        message = client.messages.create(
            from_="+14843024845",
            body= f"this otp {otp} is for verification",
            to=no
        )

        # Return message SID if successful
        return message.sid
    except Exception as e:
        print(f"Failed to send SMS: {e}")
        return None








import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = 'rishav@rishav.com'
    receiver_email = 'rishavghosh147@gmail.com'
    subject = 'Test Email'
    body = 'Hello, this is a test email sent from my custom SMTP server!'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('localhost', 25) as server:
        server.sendmail(sender_email, receiver_email, msg.as_string())

