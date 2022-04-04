from flask import request, render_template
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
    return render_template('creationEntreprise.html', creation_entreprise=creation_entreprise)


class Entreprise(object):

    def __init__(self, Nom: str = None, Siret: int = None, Adresse: str = None, Code: int = None,
                 Ville: str = None):
        self.nom = Nom
        self.siret = Siret
        self.adresse = Adresse
        self.code = Code
        self.ville = Ville