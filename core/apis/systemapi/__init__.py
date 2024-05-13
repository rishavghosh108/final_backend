from flask import Blueprint

_System=Blueprint('system',__name__)


from .mobilecheckapi import _Mobile
_System.register_blueprint(_Mobile)

from .emailcheckapi import _Email
_System.register_blueprint(_Email)

from .signupapi import _Signup
_System.register_blueprint(_Signup)

from .otpverifyapi import _Otpverify
_Signup.register_blueprint(_Otpverify)

from .loginapi import _Login
_Signup.register_blueprint(_Login)

from .profileapi import _Profile
_System.register_blueprint(_Profile)

from .forgetapi import _Forget
_System.register_blueprint(_Forget)
