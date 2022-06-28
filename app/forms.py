from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class SignUpForm(FlaskForm):
    first_name = StringField(validators=[DataRequired()])
    last_name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email(message="not a valid email")])
    mobile = IntegerField()
    country = StringField(validators=[DataRequired()])
    club = StringField(validators=[DataRequired()])
    newsletter = BooleanField('Weekly Digest')
    submit = SubmitField()