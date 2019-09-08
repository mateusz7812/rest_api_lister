from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from rest_api_lister.database.models import List, Account  # noqa
    db.drop_all()
    db.create_all()
