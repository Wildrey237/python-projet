from flask import redirect, url_for, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, BooleanField
from wtforms.validators import DataRequired

from Connexion import db
from Formulaires import FormulaireModificationClient


class Client:
    def from_email(self, email: str = None):
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
        return Client(self.Email.data, self.Entreprise.data, self.Nom.data, self.Poste.data, self.Prenom.data,
                      self.Statut.data, self.Telephone.data)


def make_client():
    creation_client = FormulaireCreationClient()
    result = render_template('creationClient.html', creation_client=creation_client)
    if creation_client.validate_on_submit():
        client = creation_client.to_model()
        client.save()
        result = redirect(url_for('test'))
    return result


def modify_client(Email):
    users_ref = db.collection(u'Client').where(u'Email', u'==', Email)
    docs = users_ref.get()
    for doc in docs:
        informations_client = doc.to_dict()
    informations_commentaire = []
    commentaire_ref = db.collection(u'Commentaire').where(u'Telephone', u'==', f"{informations_client['Telephone']}")
    commentaires = commentaire_ref.get()
    for commentaire in commentaires:
        tt = commentaire.to_dict()
        informations_commentaire.append(tt)
    formulaire_modification_client = FormulaireModificationClient()
    if formulaire_modification_client.validate_on_submit():
        Email = request.form.get('Email')
        Entreprise = request.form.get('Entreprise')
        Nom = request.form.get('Nom')
        Poste = request.form.get('Poste')
        Prenom = request.form.get('Prenom')
        Statut = request.form.get('Statut')
        Telephone = request.form.get('Telephone')
        ref_entreprise = db.collection('Client').where(u'Telephone', u'==', Telephone )
        docs = ref_entreprise.get()
        for doc in docs:
            id = doc.id
        if request.form['valider'] == 'Modifier':
            db.collection('Client').document(id).set(
                {
                    'Email': Email,
                    'Nom': Nom,
                    'Poste': Poste,
                    'Prenom': Prenom,
                    'Statut': Statut,
                    'Telephone': Telephone,
                }
            )
        elif request.form['valider'] == 'Supprimer':
            db.collection('Client').document(id).delete()
            return redirect(url_for('test'))

    return render_template('client.html', informations_client=informations_client,
                           formulaire_modification_client=formulaire_modification_client,
                           informations_commentaire=informations_commentaire)
