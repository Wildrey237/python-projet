from flask import render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, IntegerField, TextAreaField, BooleanField, SubmitField, \
    SelectField
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


class FormulaireModificationClient(FlaskForm):
    Email = EmailField(validators=[DataRequired()])
    Nom = StringField(validators=[DataRequired()])
    Poste = StringField(validators=[DataRequired()])
    Prenom = StringField(validators=[DataRequired()])
    Statut = SelectField(validators=[DataRequired()], choices=['Actif', 'Inactif'])
    Telephone = IntegerField(validators=[DataRequired()])


class FormulaireAccesEntreprise(FlaskForm):
    Siret = SubmitField()


class FormulaireFacture(FlaskForm):
    Email = EmailField(render_kw={'readonly': True})


class FormulaireRecherche(FlaskForm):
    recherche = StringField(validators=[DataRequired()])


class FormulaireRechercheContact(FlaskForm):
    Recherche = StringField(validators=[DataRequired()])


class FormulaireAjoutCommentaire(FlaskForm):
    nom = StringField(render_kw={'readonly': True})
    telephone = IntegerField(render_kw={'readonly': True})
    Commentaire = TextAreaField(validators=[DataRequired()])
