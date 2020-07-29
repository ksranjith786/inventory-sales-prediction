from flask_sqlalchemy import SQLAlchemy
from app import db

class Transaction(db.Model):
    __tablename__ = 'transactions'
    TransactionID = db.Column(
        db.Integer,
        primary_key=True
    )
    CustomerID = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    CustomerName = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    TransactionDateTime = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    SKU = db.Column(
        db.String(80),
        index=False,
        unique=False,
        nullable=True
    )
    Quantity = db.Column(
        db.Integer,
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<Customer {}>'.format(self.CustomerID)

