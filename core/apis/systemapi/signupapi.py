from flask import Blueprint
from core.apis.Schema import Signup_Schema
from core.apis.authenticate.auth import GenToken, TransformData
import os
from ..responses import APIResponse
from ..decoretor import accept_payload

_Signup=Blueprint('signup',__name__)

@_Signup.route('/signup',methods=['POST'])
@accept_payload
def Signup(incoming_payload):
    data=Signup_Schema().load(incoming_payload)
    message=APIResponse.respond({'successful':'please enter otp'})
    message.headers[os.getenv('otp_verify_header_key')]=GenToken(TransformData(data), "signup", data['user']['mobile'])
    return message