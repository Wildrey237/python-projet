from flask import request, render_template, url_for
from werkzeug.utils import redirect
from Connexion import db
from Formulaires import FormulaireCreationEntreprise, FormulaireFacture
from MakePDF import enregistre_PDF


def make_entreprise():
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


def modify_entreprise(Siret):
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
    formulaire_facture = FormulaireFacture()
    if formulaire_modification_entreprise.validate_on_submit():
        Nom = request.form.get('Nom')
        Siret = request.form.get('Siret')
        Adresse = request.form.get('Adresse')
        Code = request.form.get('Code')
        Ville = request.form.get('Ville')
        Description = request.form.get('Description')
        URL = request.form.get('URL')
        Siret = int(Siret)
        ref_entreprise = db.collection('Entreprise').where(u'Siret', u'==', Siret)
        docs = ref_entreprise.get()
        for doc in docs:
            id = doc.id
        if request.form['valider'] == 'Modifier':
            db.collection('Entreprise').document(id).set(
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
        elif request.form['valider'] == 'Supprimer':
            db.collection('Entreprise').document(id).delete()
            return redirect(url_for('test'))
    elif formulaire_facture.validate_on_submit():
        Email = request.form.get('Email')
        if request.form['contact'] == 'Acceder':
            return redirect(f'/Client-{Email}')
        elif request.form['contact'] == 'Visualiser facture':
            return redirect(f'/facture-{Email}-{Siret}')
        elif request.form['contact'] == 'Creer facture':
            enregistre_PDF(Email, Siret)
            return redirect(f'/facture-{Email}-{Siret}')

    return render_template('entreprise.html', informations_entreprise=informations_entreprise,
                           formulaire_modification_entreprise=formulaire_modification_entreprise,
                           informations_contact=informations_contact, formulaire_facture=formulaire_facture)


class Entreprise():
    def take_entreprise(self, Siret: int = None):
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
