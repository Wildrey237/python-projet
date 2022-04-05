from Connexion import db
from flask import redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, IntegerField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Client:
    def from_email(self, email :str = None):
        if email is None:
            raise Exception('Invalid request')

        docs = db.collection('Client').where(u'Email', u'==', email).get()
        users = []
        for doc in docs:
            post = doc.to_dict()
            users.append(post)
        return Client(*users[0])

    def takeClient(self, Email_contact: str = None):
        if Email_contact is None:
            docs = db.collection('Client')
        else:
            docs = db.collection('Client').where(u'Email', u'==', Email_contact)
        docs = docs.get()
        user = []
        for doc in docs:
            post = doc.to_dict()
            user.append(post)
        user = user[0]
        self.mail = user["Email"]
        """self.entreprise = user["Entreprise"]"""
        self.nom = user["Nom"]
        self.prenom = user["Prenom"]
        self.poste = user["Poste"]
        self.statut = user["Statut"]
        self.telephone = user["Telephone"]

    def __init__(self, mail: str = None, Entreprise: str = None, Nom: str = None, Poste: bool = True,
                 Prenom: str = None, Statut: str = None, Telephone: int = None):
        self.mail = mail
        self.entreprise = Entreprise
        self.nom = Nom
        self.prenom = Prenom
        self.poste = Poste
        self.statut = Statut
        self.telephone = Telephone

    def exists(self):
        "'"" Checks if a record exists in the database. """
        cli_refs = db.collection('Client').where('Telephone', '==', self.telephone).get()
        return len(cli_refs) > 0

    def save(self):
        if not self.exists():
            db.collection('Client').add(
                {
                    'Nom': self.nom,
                    'Prenom': self.prenom,
                    'Email': self.mail,
                    'Entreprise': self.entreprise,
                    'Poste': self.poste,
                    'Statut': self.statut,
                    'Telephone': self.telephone,
                }
            )
        else:
            # TODO : please implement the update of a record !!
            pass


class FormulaireCreationClient(FlaskForm):
    Nom = StringField(validators=[DataRequired()])
    Prenom = StringField(validators=[DataRequired()])
    Email = EmailField(validators=[DataRequired()])
    Entreprise = StringField(validators=[DataRequired()])
    Poste = StringField(validators=[DataRequired()])
    Statut = BooleanField(validators=[DataRequired()])
    Telephone = IntegerField(validators=[DataRequired()])

    def to_model(self):
        return Client(self.Email.data, self.Entreprise.data, self.Nom.data, self.Poste.data, self.Prenom.data, self.Statut.data, self.Telephone.data)

def makeClient():
    creation_client = FormulaireCreationClient()
    if creation_client.validate_on_submit():
        client = creation_client.to_model()
        client.save()
        return redirect(url_for('test'))
    return render_template('creationClient.html', creation_client=creation_client)
