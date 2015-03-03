from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class User(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
