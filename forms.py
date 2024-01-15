from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class loginForm(FlaskForm):
    email = StringField('email',render_kw={"placeholder":"Enter Email ID"}, validators=[DataRequired(), Email()])
    password = PasswordField('Password',render_kw={"placeholder":"Enter Password"}, validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField("Login")

class registrationForm(FlaskForm):
    Name = StringField('name',render_kw={"placeholder":'Enter Name'},validators=[DataRequired(),Length(min=3, max=20)])
    email = StringField('Email ID', render_kw={"placeholder":'Enter Email ID'},validators=[DataRequired(),Email()])
    password = PasswordField("Password",render_kw={"placeholder":'Enter Password'},validators=[DataRequired(),Length(min=3, max=8)])
    confirmPassword = PasswordField("confirmPassword",render_kw={"placeholder":'Confirm Password'},validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField("Sign Up")