from urllib import request

from flask import render_template, request
from formulaires import FormulaireCreationClient
from connexion import db


class Client:
    def Takeclient(self, Email: str = None):
        if Email is None:
            docs = db.collection('Client')
        else:
            docs = db.collection('Client').where(u'Email', u'==', Email)
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


def makeClient():
    creation_client = FormulaireCreationClient()
    if creation_client.validate_on_submit():
        Nom = request.form.get('Nom')
        Prenom = request.form.get('Prenom')
        Email = request.form.get('Email')
        Entreprise = request.form.get('Entreprise')
        Poste = request.form.get('Poste')
        Statut = request.form.get('Statut')
        Telephone = request.form.get('Telephone')
        db.collection('Client').add(
            {
                'Nom': Nom,
                'Prenom': Prenom,
                'Email': Email,
                'Entreprise': Entreprise,
                'Poste': Poste,
                'Statut': Statut,
                'Telephone': Telephone,
            }
        )
    return render_template('creationClient.html', creation_client=creation_client)
