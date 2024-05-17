from flask import Blueprint
from core.apis.Schema import EmailSchema
from core.model.Email import Email
from core.apis.decoretor import authorization_payload
from core.apis.authenticate.auth import Decrept_email
from ..responses import APIResponse

_Inbox=Blueprint('inbox',__name__)

@_Inbox.route('/inbox',methods=['GET'])
@authorization_payload
def Inbox(token):
    email=Decrept_email(token)
    data=Email.get_Inbox(email)
    dump_data=EmailSchema(many=True).dump(data)
    return APIResponse.respond(dump_data)