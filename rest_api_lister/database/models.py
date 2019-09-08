# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from rest_api_lister.database import db


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    account = db.relationship('Account', backref=db.backref('lists', lazy='dynamic'))

    def __init__(self, title, body, account, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.account = account

    def __repr__(self):
        return '<List %r>' % self.title


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(50))
    contacts = db.Column(db.String(200))

    def __init__(self, nick):
        self.nick = nick

    def __repr__(self):
        return '<Account %r>' % self.nick
