from flask import Blueprint
from core.apis.Schema import Email_Schema
from core.model.username import Username
from ..responses import APIResponse
from ..decoretor import accept_payload

_Email=Blueprint('email',__name__)

@_Email.route('/email',methods=['POST'])
@accept_payload
def Check(incoming_payload):
    emailid=Email_Schema().load(incoming_payload)
    check=Username.GetEmail(emailid['email'].lower())
    if check is None:
        return APIResponse.respond({'successful':'false'})
    else:
        return APIResponse.respond({'successful':'true'})