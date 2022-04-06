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
        facture_ref = db.collection('Facture').where(u'SiretEntreprise', u'==', entreprise_todict['Siret'])
        factures = facture_ref.get()
        nb_facture = len(factures)
        dic_facture = {'Facture' : nb_facture}
        entreprise_todict.update(dic_facture)
        liste_entreprise.append(entreprise_todict)
    if liste_entreprise == []:
        return redirect('/Homepage')
    formulaire_acces_entreprise = FormulaireAccesEntreprise()
    formulaire_recherche = FormulaireRecherche()
    result = render_template('homepage.html', liste_entreprise=liste_entreprise,
                             formulaire_acces_entreprise=formulaire_acces_entreprise,
                             formulaire_recherche=formulaire_recherche)
    if formulaire_recherche.validate_on_submit():
        recherche = request.form['recherche']
        return redirect(f'/Recherche-{recherche}')
    return result

