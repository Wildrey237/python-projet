from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, EmailField, IntegerField, DecimalField
from wtforms.validators import DataRequired


class ConnexionFormulaire(FlaskForm):
    Email = EmailField(validators=[DataRequired()])
    Password = PasswordField(validators=[DataRequired()])


class FormulaireCreationEntreprise(FlaskForm):
    Nom = StringField(validators=[DataRequired()])
    Siret = IntegerField(validators=[DataRequired()])
    Adresse = StringField(validators=[DataRequired()])
    Code = IntegerField(validators=[DataRequired()])
    Ville = StringField(validators=[DataRequired()])
    Description = StringField
    URL = StringField
