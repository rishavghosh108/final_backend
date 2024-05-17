from flask import Blueprint

_App=Blueprint('app',__name__)

from .inbox import _Inbox
_App.register_blueprint(_Inbox)

from .starred import _Starred
_App.register_blueprint(_Starred)

from .sent import _Sent
_App.register_blueprint(_Sent)

from .spam import _Spam
_App.register_blueprint(_Spam)

from .bin import _Bin
_App.register_blueprint(_Bin)