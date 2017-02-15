from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, ValidationError
from app.models.user import User

def notExisting(form, field):
    print(field.data)
    usrs = User.query.with_entities(User.username).all()
    if (field.data,) in usrs:
        raise ValidationError('Username already in use!')
    else:
        print("ok")


class registerForm(Form):
    name = StringField(20)
    username = StringField(20, [DataRequired(), notExisting])
    password = PasswordField(40)
    email = StringField(40, [DataRequired(), Email(message="E-mail not valid")])
    submit = SubmitField("Sign Up")

