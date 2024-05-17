from flask import Blueprint
from core.apis.Schema import EmailSchema
from core.model.Email import Email
from core.apis.decoretor import authorization_payload
from core.apis.authenticate.auth import Decrept_email
from ..responses import APIResponse

_Bin=Blueprint('bin',__name__)

@_Bin.route('/bin',methods=['GET'])
@authorization_payload
def Bin(token):
    email=Decrept_email(token)
    data=Email.get_Bin(email)
    dump_data=EmailSchema(many=True).dump(data)
    return APIResponse.respond(dump_data)