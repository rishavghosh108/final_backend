from flask import Blueprint
from ..decoretor import authorization_payload
from core.apis.authenticate.auth import Decrept_email
from core.apis.responses import APIResponse
from core.model.username import Username
from core.model.user import User

_Profile=Blueprint('profile',__name__)

@_Profile.route('/profile',methods=['POST'])
@authorization_payload
def Profile(token):
    email=Decrept_email(token)
    user=Username.Profile(email)
    data=User.Profile(user)
    return APIResponse.respond({"successful":data})