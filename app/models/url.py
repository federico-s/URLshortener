import string

from app import db
from app.models import user

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(6))
    long_url = db.Column(db.String(100))
    short_url = db.Column(db.String(20))
    author = db.Column(db.Integer, db.ForeignKey("user.id"))

    def code_generator(chars=string.ascii_letters + string.digits):
        import random
        size = 6
        return ''.join(random.choice(chars) for _ in range(size))

    def addProtocol(url):
        if not url.startswith("http://") and not url.startswith("https://"):
            return "http://"+url
        return url