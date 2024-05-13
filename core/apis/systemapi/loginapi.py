from flask import Blueprint
from ..responses import APIResponse
from ..decoretor import accept_payload
from core.model.username import Username
from ..Schema import Username_Schema
import os

_Login=Blueprint('login',__name__)

@_Login.route('/login',methods=['POST'])
@accept_payload
def Login(incoming_payload):
    data=Username_Schema().load(incoming_payload)
    token=Username.Login(data)
    message=APIResponse.respond({"successful":"login successful"})
    message.headers[os.getenv('authorization_header_key')]=token
    return message