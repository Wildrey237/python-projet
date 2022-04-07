import datetime
from flask import request, render_template, session, redirect
from Connexion import db
from Formulaires import FormulaireAjoutCommentaire


def info_client(telephone):
    telephone = int(telephone)
    refs = db.collection('Client').where('Telephone', '==', telephone)
    identifiant = refs.get()
    return identifiant


def make_commentaire(telephone):
    client = info_client(telephone)
    form_commentaire = FormulaireAjoutCommentaire()

    nom_client = client[0].get('Nom')
    temps_commentaire = datetime.datetime.now()

    if form_commentaire.validate_on_submit():
        commentaire = request.form.get('Commentaire')
        db.collection('Commentaire').add(
            {
                'Nom': session['Email'],
                'Telephone': telephone,
                'Commentaire': commentaire,
                'Date de création': temps_commentaire
            }
        )
        return redirect('/Homepage')
    return render_template('ajoutCommentaire.html', commentaire=form_commentaire, nom_client=nom_client)