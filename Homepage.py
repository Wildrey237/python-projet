from flask import render_template, redirect, url_for, request
from Formulaires import FormulaireAccesEntreprise, FormulaireRecherche
from Connexion import db



def page_test(recherche):
    if recherche == None:
        collection_entreprise = db.collection(u'Entreprise').order_by('Nom')
    else:
        collection_entreprise = db.collection(u'Entreprise').where(u'Nom', u'==', recherche)
    dictionnaire_entreprise = collection_entreprise.get()
    liste_entreprise = []
    for entreprise in dictionnaire_entreprise:
        entreprise_todict = entreprise.to_dict()
        liste_entreprise.append(entreprise_todict)
    if liste_entreprise == []:
        return redirect('/Homepage')
    formulaire_acces_entreprise = FormulaireAccesEntreprise()
    formulaire_recherche = FormulaireRecherche()
    result = render_template('homepage.html', liste_entreprise=liste_entreprise,
                             formulaire_acces_entreprise=formulaire_acces_entreprise,
                             formulaire_recherche=formulaire_recherche,
                             formulaire_recherche_contact=formulaire_recherche_contact)
    if formulaire_recherche.validate_on_submit():
        recherche = request.form['recherche']
        return redirect(f'/Recherche-{recherche}')
    return result

