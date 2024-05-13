from flask import Blueprint
from ..responses import APIResponse
from ..decoretor import accept_payload
from ..Schema import Username_Schema
from core.model.username import Username
from core.model.user import User
from core.apis.authenticate.auth import GenToken, GenPasswordHash
import os

_Forget=Blueprint('forget',__name__)

@_Forget.route('/forget',methods=['POST'])
@accept_payload
def Forget(incoming_payload):
    data=Username_Schema().load(incoming_payload)
    username=Username.Profile(data['email'])
    user=User.user(username)
    message=APIResponse.respond({"successful":"please enter the otp"})
    message.headers[os.getenv('otp_verify_header_key')]=GenToken({"email":username.email,"password":GenPasswordHash(data['password'])}, "forget", user.mobile)
    return message