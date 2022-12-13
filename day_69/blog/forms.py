from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

# WTForm


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterUserForm(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired()])
    email = EmailField("Your email", validators=[DataRequired()])
    password = PasswordField("YourPassword", validators=[DataRequired()])
    submit = SubmitField("Register now")


class LoginUserForm(FlaskForm):
    email = EmailField("Your email", validators=[DataRequired()])
    password = PasswordField("YourPassword", validators=[DataRequired()])
    submit = SubmitField("Login")


class CommentForm(FlaskForm):
    comment = CKEditorField("comment", validators=[DataRequired()])
    submit = SubmitField("Post a comment")
