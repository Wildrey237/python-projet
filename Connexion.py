from flask import redirect, request, url_for, render_template, session
from Formulaires import ConnexionFormulaire
from ConnectDb import connect_BD
import time

db = connect_BD()


def connexion():
    connexion_formulaire = ConnexionFormulaire()
    result = render_template('connexion.html', connexion_formulaire=connexion_formulaire)
    if connexion_formulaire.validate_on_submit():
        Email = request.form['Email']
        Password = request.form['Password']
        users_ref = db.collection(u'Users').where(u'Email', u'==', Email)
        docs = users_ref.get()
        for doc in docs:
            test = doc.to_dict()
            if test["Password"] == f'{Password}':
                session['duree'] = time.time() + 3600  # Durée en seconde de la session
                print('bv')
                result = redirect(url_for('test'))
            else:
                result = redirect(url_for('connexion_test'))
    return result
