import datetime

from flask import request, render_template

from Connexion import db
from Formulaires import FormulaireAjoutCommentaire


class Commentaire(object):

    def __init__(self):
        pass


def infoClient(telephone):
    refs = db.collection('Client').where('Telephone', '==', telephone)
    identifiant = refs.get()
    return identifiant


def makeCommentaire(telephone):
    client = infoClient(telephone)
    form_commentaire = FormulaireAjoutCommentaire()

    form_commentaire.nom.data = client[0].get('Nom')
    form_commentaire.telephone.data = client[0].get('Telephone')
    temps_commentaire = datetime.datetime.now()

    if form_commentaire.validate_on_submit():
        commentaire = request.form.get('Commentaire')
        db.collection('Commentaire').add(
            {
                'Nom': form_commentaire.nom.data,
                'Telephone': form_commentaire.telephone.data,
                'Commentaire': commentaire,
                'Date de création': temps_commentaire
            }
        )
    return render_template('ajoutCommentaire.html', commentaire=form_commentaire)
