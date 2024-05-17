from flask import Blueprint
from core.apis.Schema import EmailSchema
from core.model.Email import Email
from core.apis.decoretor import authorization_payload
from core.apis.authenticate.auth import Decrept_email
from ..responses import APIResponse

_Spam=Blueprint('spam',__name__)

@_Spam.route('/spam',methods=['GET'])
@authorization_payload
def Spam(token):
    email=Decrept_email(token)
    data=Email.get_Spam(email)
    dump_data=EmailSchema(many=True).dump(data)
    return APIResponse.respond(dump_data)