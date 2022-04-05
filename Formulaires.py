from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, IntegerField, TextAreaField, BooleanField, SubmitField
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
    Description = TextAreaField()
    URL = StringField()


class FormulaireCreationClient(FlaskForm):
    Nom = StringField(validators=[DataRequired()])
    Prenom = StringField(validators=[DataRequired()])
    Email = EmailField(validators=[DataRequired()])
    Entreprise = StringField(validators=[DataRequired()])
    Poste = StringField(validators=[DataRequired()])
    Statut = BooleanField(validators=[DataRequired()])
    Telephone = IntegerField(validators=[DataRequired()])


class FormulaireAccesEntreprise(FlaskForm):
    Siret = SubmitField()


class FormulaireAjoutCommentaire(FlaskForm):
    nom = StringField()
    telephone = IntegerField()
    Commentaire = TextAreaField(validators=[DataRequired()])


