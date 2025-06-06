from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.modals import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username = username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists, try a different one')
    def validate_email_address(self, email_address_to_check):
        emailad = User.query.filter_by(email_address=email_address_to_check.data).first()
        if emailad:
            raise ValidationError("Already exists,try a different one")
        

    username = StringField(label='User Name',validators =[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email',validators = [Email(), DataRequired()])
    password = PasswordField(label = 'Password', validators = [Length(min=6), DataRequired()])
    confirm = PasswordField(label = 'Confirm Password', validators = [EqualTo('password'), DataRequired()])
    submit = SubmitField(label = 'Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators= [DataRequired()])
    password =PasswordField(label='Password',validators=[DataRequired()])
    submit = SubmitField(label = 'Submit')

class PurchaseForm(FlaskForm):
    submit = SubmitField(label = 'Purchase Item')

class SellForm(FlaskForm):
    submit = SubmitField(label = 'Sell Item')