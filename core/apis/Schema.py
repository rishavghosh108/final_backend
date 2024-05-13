from marshmallow import Schema, ValidationError,fields, validate

def validate_mobile(value):
        if len(str(value)) != 10:
            raise ValidationError('Mobile number must be exactly 10 digits')
        
def validate_otp(value):
        if len(str(value)) != 4:
            raise ValidationError('Otp must be exactly 4 digits')

class Mobile_Scheam(Schema):
    mobile=fields.Integer(required=True, validate=validate_mobile)

class Email_Schema(Schema):
    email=fields.Email(required=True)

class User_Schema(Schema):
    name=fields.String(required=True)
    gender=fields.String(required=True, validate=validate.OneOf(["male", "female"]))
    dob=fields.Date(required=True)
    mobile=fields.Integer(required=True, validate=validate_mobile)

class Username_Schema(Schema):
    email=fields.Email(required=True)
    password=fields.String(required=True)

class Signup_Schema(Schema):
    user=fields.Nested(User_Schema)
    username=fields.Nested(Username_Schema)

class Otp_Schema(Schema):
    otp=fields.Integer(required=True, validate=validate_otp)