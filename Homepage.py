from flask import render_template, redirect, url_for, request
from Formulaires import FormulaireAccesEntreprise
from Connexion import db


def page_test():
    collection_entreprise = db.collection(u'Entreprise').order_by('Nom')
    dictionnaire_entreprise = collection_entreprise.get()
    liste_entreprise = []
    for entreprise in dictionnaire_entreprise:
        entreprise_todict = entreprise.to_dict()
        liste_entreprise.append(entreprise_todict)
    formulaire_acces_entreprise = FormulaireAccesEntreprise()
    result = render_template('homepage.html', liste_entreprise=liste_entreprise,formulaire_acces_entreprise=formulaire_acces_entreprise)
    if formulaire_acces_entreprise.validate_on_submit():
        Siret = request.form['Siret']
        result = redirect(f'/Entreprise-{Siret}')
    return result

