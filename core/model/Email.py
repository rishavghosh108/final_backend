from core import db
from datetime import datetime
from sqlalchemy.types import Enum as BaseEnum
import enum

class TypeEnum(str, enum.Enum):
    spam = 'SPAM'
    bin = 'BIN'
    sent = 'SENT'
    inbox = 'INBOX'
    starred = 'STARRED'


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(120), nullable=False)
    recipient = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200))
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default= datetime.utcnow, nullable=False)
    type = db.Column(BaseEnum(TypeEnum))

    @classmethod
    def filter(cls, *criterion):
        db_query = db.session.query(cls)
        return db_query.filter(*criterion)
    
    @classmethod
    def get_Inbox(cls, email):
        return cls.filter(cls.type == TypeEnum.inbox, cls.recipient == email).all()
    
    @classmethod
    def get_Starred(cls, email):
        return cls.filter(cls.type == TypeEnum.starred, cls.recipient == email).all()
    
    @classmethod
    def get_Bin(cls, email):
        return cls.filter(cls.type == TypeEnum.bin, cls.recipient == email).all()
    
    @classmethod
    def get_Spam(cls, email):
        return cls.filter(cls.type == TypeEnum.spam, cls.recipient == email).all()
    
    @classmethod
    def get_Sent(cls, email):
        return cls.filter(cls.type == TypeEnum.sent, cls.sender == email).all()