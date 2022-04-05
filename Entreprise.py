from flask import request, render_template, url_for
from werkzeug.utils import redirect

from Connexion import db
from Formulaires import FormulaireCreationEntreprise


class Entreprise(object):

    def __init__(self, Nom: str = None, Siret: int = None, Adresse: str = None, Code: int = None,
                 Ville: str = None):
        self.nom = Nom
        self.siret = Siret
        self.adresse = Adresse
        self.code = Code
        self.ville = Ville


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
    informations_entreprise = []
    users_ref = db.collection(u'Entreprise').where(u'Siret', u'==', Siret)
    docs = users_ref.get()
    for doc in docs:
        test = doc.to_dict()
    informations_entreprise.append(test)
    return render_template('entreprise.html', informations_entreprise=informations_entreprise)