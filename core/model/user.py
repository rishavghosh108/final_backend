from datetime import datetime
from core import db
from enum import Enum
from sqlalchemy.types import Enum as BaseEnum
from core.model.username import Username

class Gender(str, Enum):
    MALE='male'
    FEMALE='female'

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    gender=db.Column(BaseEnum(Gender), nullable=False)
    dob=db.Column(db.Date, nullable=False)
    mobile=db.Column(db.Integer, nullable=False)

    # username=db.relationship('Username', backref='user', lazy=True)

    @classmethod
    def filter(cls,*criterion):
        db_query=db.session.query(cls)
        return db_query.filter(*criterion)

    @classmethod
    def GetMobile(cls,no):
        return cls.filter(cls.mobile==no).first()
    
    @classmethod
    def Update(cls,token_data):
        data=token_data['data']
        if token_data["type"]=="signup":
            dob = datetime.strptime(data['user']['dob'], "%Y-%m-%d").date()
            user=cls(name=data["user"]["name"],gender=data["user"]["gender"],dob=dob,mobile=data["user"]["mobile"])
            db.session.add(user)
            db.session.flush()
            Username.Signup(data["username"], user.id)
            db.session.commit()
        else:
            Username.Forget(data)
            

    @classmethod
    def Profile(cls, user):
        found_user=cls.filter(cls.id==user.id).first()
        return {"email": user.email, "name": found_user.name}
    
    @classmethod
    def user(cls, user):
        return cls.filter(cls.id==user.id).first()