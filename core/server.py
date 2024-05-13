from core import app
from flask import jsonify
from flask_cors import CORS
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from core.libs.exceptions import ProjectError
import os

from core.apis.systemapi import _System

app.register_blueprint(_System,url_prefix="/system")

# CORS(app, resources={r"*": {"origins": "*"}}, methods=['POST','GET'], expose_headers=['Content-Type','Access-Control-Allow-Origin','auth','verification'])

CORS(
    app,
    resources={r"*": {"origins": "*"}},
    methods=['POST', 'GET'],
    expose_headers=['Content-Type', 'Access-Control-Allow-Origin', os.getenv('authorization_header_key'), os.getenv('otp_verify_header_key')],
    allow_headers=['Content-Type',  os.getenv('otp_verify_header_key'), os.getenv('authorization_header_key')]
)



@app.errorhandler(Exception)
def handle_error(err):
    if isinstance(err, ProjectError):
        return jsonify(
            error=err.__class__.__name__, message=err.message
        ), err.status_code
    elif isinstance(err, ValidationError):
        return jsonify(
            error=err.__class__.__name__, message=err.messages
        ), 400
    elif isinstance(err, IntegrityError):
        return jsonify(
            error=err.__class__.__name__, message=str(err.orig)
        ), 400
    elif isinstance(err, HTTPException):
        return jsonify(
            error=err.__class__.__name__, message=str(err)
        ), err.code
    raise err