import hashlib

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password = db.Column(db.String(40))
    email = db.Column(db.String(30))

    def hashPassword(pwd):
        hash_object = hashlib.sha1(pwd.encode())
        return hash_object.hexdigest()