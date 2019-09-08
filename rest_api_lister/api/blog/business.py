from rest_api_lister.database import db
from rest_api_lister.database.models import List, Account


def create_list(data):
    title = data.get('title')
    body = data.get('body')
    account_id = data.get('account_id')
    account = Account.query.filter(Account.id == account_id).one()
    lister_list = List(title, body, account)
    db.session.add(lister_list)
    db.session.commit()


def update_list(list_id, data):
    lister_list = List.query.filter(List.id == list_id).one()
    lister_list.title = data.get('title')
    lister_list.body = data.get('body')
    account_id = data.get('account_id')
    lister_list.account = Account.query.filter(Account.id == account_id).one()
    db.session.add(lister_list)
    db.session.commit()


def delete_list(list_id):
    lister_list = List.query.filter(List.id == list_id).one()
    db.session.delete(lister_list)
    db.session.commit()


def create_account(data):
    nick = data.get('nick')
    account_id = data.get('id')

    account = Account(nick)
    if account_id:
        account.id = account_id

    db.session.add(account)
    db.session.commit()


def update_account(account_id, data):
    account = Account.query.filter(Account.id == account_id).one()
    account.nick = data.get('nick')
    db.session.add(account)
    db.session.commit()


def delete_account(account_id):
    account = Account.query.filter(Account.id == account_id).one()
    db.session.delete(account)
    db.session.commit()
