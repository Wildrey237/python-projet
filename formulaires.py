from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, EmailField, IntegerField, DecimalField
from wtforms.validators import DataRequired


class ConnexionFormulaire(FlaskForm):
    Email = EmailField(validators=[DataRequired()])
    Password = PasswordField(validators=[DataRequired()])