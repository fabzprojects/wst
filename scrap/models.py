from enum import unique
from ssl import _create_unverified_context
from scrap import db,app,login_manager
from flask_login import UserMixin
from flask_table import Table, Col, LinkCol


@login_manager.user_loader
def load_user(id):
    return Login.query.get(int(id))






# class Login(db.Model, UserMixin):
#     id=db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80))
#     password = db.Column(db.String(80), nullable=False)
#     usertype = db.Column(db.String(80), nullable=False)
#     name = db.Column(db.String(200))
#     address = db.Column(db.String(200))
#     contact = db.Column(db.String(200))
#     shop = db.Column(db.String(200))
#     approve = db.Column(db.String(200))
#     reject = db.Column(db.String(200))
#     ret_id= db.Column(db.String(200))





# class Contact(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(200))
#     email= db.Column(db.VARCHAR)
#     subject= db.Column(db.VARCHAR)
#     message= db.Column(db.String(200))



