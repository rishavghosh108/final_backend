from flask import Blueprint
from core.apis.Schema import EmailSchema
from core.model.Email import Email
from ..decoretor import authorization_payload
from core.apis.authenticate.auth import Decrept_email
from ..responses import APIResponse

_Sent=Blueprint('sent',__name__)

@_Sent.route('/sent',methods=['GET'])
@authorization_payload
def Sent(token):
    email=Decrept_email(token)
    data=Email.get_Sent(email)
    dump_data=EmailSchema(many=True).dump(data)
    return APIResponse.respond(dump_data)