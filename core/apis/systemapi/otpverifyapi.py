from flask import Blueprint
from ..decoretor import accept_payload, verification_payload
from ..Schema import Otp_Schema
from core.apis.responses import APIResponse
from core.apis.authenticate.auth import Decript
from core.model.user import User

_Otpverify=Blueprint('otpverify',__name__)

@_Otpverify.route('/otpverify',methods=['POST'])
@verification_payload
@accept_payload
def otp_validate(incoming_payload,token):
    otp=Otp_Schema().load(incoming_payload)
    data=Decript(token, otp)
    User.Update(data)
    return APIResponse.respond({"successful":"true"})