from core import db
from werkzeug.security import check_password_hash
from core.libs.assertions import assert_valid,assert_found
from core.apis.authenticate.auth import Authorization

class Username(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(500), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @classmethod
    def filter(cls, *criterion):
        db_query = db.session.query(cls)
        return db_query.filter(*criterion)

    @classmethod
    def GetEmail(cls, email):
        return cls.filter(cls.email == email).first()
    
    @classmethod
    def Signup(cls, data, id):
        username=cls(email=data["email"],password=data["password"],user_id=id)
        db.session.add(username)
        db.session.commit()
        return True
    
    @classmethod
    def Login(cls, data):
        user=cls.filter(cls.email==data['email']).first()
        assert_found(user,"email not found")
        assert_valid(check_password_hash(user.password,data['password']),"wrong password")
        return Authorization(data['email'])
    
    @classmethod
    def Profile(cls, email):
        user=cls.filter(cls.email==email).first()
        return user
    
    @classmethod
    def Forget(cls, data):
        user=cls.filter(cls.email==data['email']).first()
        user.password=data['password']
        db.session.commit()
        return True