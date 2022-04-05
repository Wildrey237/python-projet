from flask import request, render_template, url_for
from werkzeug.utils import redirect

from Connexion import db
from Formulaires import FormulaireCreationEntreprise


def makeEntreprise():
    creation_entreprise = FormulaireCreationEntreprise()
    if creation_entreprise.validate_on_submit():
        Nom = request.form.get('Nom')
        Siret = request.form.get('Siret')
        Adresse = request.form.get('Adresse')
        Code = request.form.get('Code')
        Ville = request.form.get('Ville')
        Description = request.form.get('Description')
        URL = request.form.get('URL')

        ent_refs = db.collection('Entreprise').where('Siret', '==', Siret)
        refs = ent_refs.get()

        if refs:
            for ref in refs:
                check = ref.to_dict()
                if check['Siret'] == Siret:
                    return redirect(url_for('test'))
        else:
            db.collection('Entreprise').add(
                {
                    'Nom': Nom,
                    'Siret': Siret,
                    'Adresse': Adresse,
                    'Code': Code,
                    'Ville': Ville,
                    'Description': Description,
                    'URL': URL,
                }
            )
        return redirect(url_for('test'))
    return render_template('creationEntreprise.html', creation_entreprise=creation_entreprise)


def modifyEntreprise(Siret):
    Siret = int(Siret)
    users_ref = db.collection(u'Entreprise').where(u'Siret', u'==', Siret)
    docs = users_ref.get()
    for doc in docs:
        informations_entreprise = doc.to_dict()
    informations_contact = []
    contact_ref = db.collection(u'Client').where(u'Entreprise', u'==', informations_entreprise['Nom'])
    contacts = contact_ref.get()
    for contact in contacts:
        tt = contact.to_dict()
        informations_contact.append(tt)

    formulaire_modification_entreprise = FormulaireCreationEntreprise()
    return render_template('entreprise.html', informations_entreprise=informations_entreprise,
                           formulaire_modification_entreprise=formulaire_modification_entreprise,
                           informations_contact=informations_contact)


class Entreprise():
    def takeEntreprise(self, Siret: int = None):
        if Siret is None:
            docs = db.collection('Entreprise')
        else:
            docs = db.collection('Entreprise').where(u'Siret', u'==', Siret)
        docs = docs.get()
        entreprise = []
        for doc in docs:
            post = doc.to_dict()
            entreprise.append(post)
        entreprise = entreprise[0]
        self.nom = entreprise['Nom']
        self.siret = entreprise['Siret']
        self.adresse = entreprise['Adresse']
        self.code = entreprise['Code']
        self.ville = entreprise['Ville']
        self.url = entreprise['URL']
        self.description = entreprise['Description']

    def __init__(self, Nom: str = None, Siret: int = None, Adresse: str = None, Code: int = None,
                 Ville: str = None, URL: str = None, Description: str = None):
        self.nom = Nom
        self.siret = Siret
        self.adresse = Adresse
        self.code = Code
        self.ville = Ville
        self.url = URL
        self.description = Description

