from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired
import re

def invalidUrl(form, field):
    pattern = re.compile("https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’])")
    print(field.data)
    print(pattern.match(field.data))
    if pattern.match(field.data) is None:
        raise ValidationError('Invalid URL.')
    else:
        print("OK")

class urlForm(Form):
    long_url = StringField(200, [DataRequired(), invalidUrl])
    submit = SubmitField("Shortenify")
