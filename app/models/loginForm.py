from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models.user import User

def CheckCredentials(form, field):
    usrs = User.query.with_entities(User.username).all()
    if (field.data,) not in usrs:
        raise ValidationError('Invalid credentials!')
    else:
        usrs = User.query.filter_by(username=field.data).with_entities(User.password).first()
        if (User.hashPassword(form.password.data),)[0] != usrs.password:
            raise ValidationError('Invalid credentials!')
        else:
            print("ok")


def PasswordCorrect(form, field):
    usrs = User.query.with_entities(User.username, User.password).all()
    if (field.data,) not in usrs:
        raise ValidationError('Invalid credentials!')
    else:
        print("ok")


class loginForm(Form):
    username = StringField(20, [DataRequired(), CheckCredentials])
    password = PasswordField(40, [DataRequired()])#, PasswordCorrect])
    submit = SubmitField("Sign Up")

