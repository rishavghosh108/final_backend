from flask import Blueprint
from core.apis.Schema import Mobile_Scheam
from core.model.user import User
from ..responses import APIResponse
from ..decoretor import accept_payload

_Mobile=Blueprint('mobile',__name__)

@_Mobile.route('/mobile',methods=['POST'])
@accept_payload
def Check(incoming_payload):
    mobileno=Mobile_Scheam().load(incoming_payload)
    check=User.GetMobile(mobileno['mobile'])
    if check is None:
        return APIResponse.respond(data={'successful':'false'})
    else:
        return APIResponse.respond(data={'successful':'true'})