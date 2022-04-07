from flask import request, render_template, url_for
from werkzeug.utils import redirect
from Connexion import db
from Formulaires import FormulaireCreationEntreprise, FormulaireFacture
from MakePDF import enregistre_PDF


def make_entreprise():
    creation_entreprise = FormulaireCreationEntreprise()
    result = render_template('creationEntreprise.html', creation_entreprise=creation_entreprise)
    if creation_entreprise.validate_on_submit():
        nom = request.form.get('Nom')
        siret = request.form.get('Siret')
        adresse = request.form.get('Adresse')
        code = request.form.get('Code')
        ville = request.form.get('Ville')
        description = request.form.get('Description')
        url = request.form.get('URL')
        siret = int(siret)

        ent_refs = db.collection('Entreprise').where('Siret', '==', siret)
        refs = ent_refs.get()

        if refs:
            for ref in refs:
                check = ref.to_dict()
                if check['Siret'] == siret:
                    return redirect(url_for('test'))
        else:
            db.collection('Entreprise').add(
                {
                    'Nom': nom,
                    'Siret': siret,
                    'Adresse': adresse,
                    'Code': code,
                    'Ville': ville,
                    'Description': description,
                    'URL': url,
                }
            )
        result = redirect(url_for('Homepage'))
    return result


def modify_entreprise(siret):
    siret = int(siret)
    users_ref = db.collection(u'Entreprise').where(u'Siret', u'==', siret)
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
    formulaire_facture = FormulaireFacture()
    result = render_template('entreprise.html', informations_entreprise=informations_entreprise,
                             formulaire_modification_entreprise=formulaire_modification_entreprise,
                             informations_contact=informations_contact, formulaire_facture=formulaire_facture)
    if formulaire_modification_entreprise.validate_on_submit():
        nom = request.form.get('Nom')
        siret = request.form.get('Siret')
        adresse = request.form.get('Adresse')
        code = request.form.get('Code')
        ville = request.form.get('Ville')
        description = request.form.get('Description')
        url = request.form.get('URL')
        siret = int(siret)
        ref_entreprise = db.collection('Entreprise').where(u'Siret', u'==', siret)
        docs = ref_entreprise.get()
        for doc in docs:
            id = doc.id
        if request.form['valider'] == 'Modifier':
            db.collection('Entreprise').document(id).set(
                {
                    'Nom': nom,
                    'Siret': siret,
                    'Adresse': adresse,
                    'Code': code,
                    'Ville': ville,
                    'Description': description,
                    'URL': url,
                }
            )
            result = redirect(url_for('Homepage'))
        elif request.form['valider'] == 'Supprimer':
            db.collection('Entreprise').document(id).delete()
            result = redirect(url_for('Homepage'))
    elif formulaire_facture.validate_on_submit():
        email = request.form.get('Email')
        if request.form['contact'] == 'Acceder':
            result = redirect(f'/Client-{email}')
        elif request.form['contact'] == 'Visualiser facture':
            result = redirect(f'/facture-{email}-{siret}')
        elif request.form['contact'] == 'Creer facture':
            enregistre_PDF(email, siret)
            result = redirect(f'/facture-{email}-{siret}')
    return result


class Entreprise():
    def take_entreprise(self, siret: int = None):
        if siret is None:
            docs = db.collection('Entreprise')
        else:
            docs = db.collection('Entreprise').where(u'Siret', u'==', siret)
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

    def __init__(self, nom: str = None, siret: int = None, adresse: str = None, code: int = None,
                 ville: str = None, url: str = None, description: str = None):
        self.nom = nom
        self.siret = siret
        self.adresse = adresse
        self.code = code
        self.ville = ville
        self.url = url
        self.description = description
