from . import db
from sqlalchemy.sql import func


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(200), nullable=False)
    lastName = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    funds = db.relationship('Funds', backref='Users')

    def __repr__(self):
        return f'<User  {self.firstName} {self.id}>'


class Funds(db.Model):
    __tablename__ = "Funds"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Numeric(10, 2))
    userId = db.Column(db.Integer, db.ForeignKey('Users.id'))
    # created_by = db.Column(db.Integer, db.ForeignKey('Users.firstName'))
    # updated_by = db.Column(db.Integer, db.ForeignKey('Users.firstName'))
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    @property
    def putserialize(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'updated_at': self.updated_at
        }