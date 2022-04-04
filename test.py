from flask import render_template, redirect, url_for
from formulaires import FormulaireAccesEntreprise
from connexion import db


def page_test():
    collection_entreprise = db.collection(u'Entreprise')
    dictionnaire_entreprise = collection_entreprise.get()
    liste_entreprise = []
    for entreprise in dictionnaire_entreprise:
        entreprise_todict = entreprise.to_dict()
        liste_entreprise.append(entreprise_todict)
    formulaire_acces_entreprise = FormulaireAccesEntreprise()
    if formulaire_acces_entreprise.validate_on_submit():
        Siret = request.form['Siret']
        informations_entreprise = []
        return redirect(url_for('entreprise', Siret=Siret))
    return render_template('test.html', liste_entreprise=liste_entreprise, formulaire_acces_entreprise=formulaire_acces_entreprise)

