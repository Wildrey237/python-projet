from flask import redirect, request, url_for, render_template, session
from Formulaires import ConnexionFormulaire
from ConnectDb import connect_BD
import time

db = connect_BD()


def connexion():
    connexion_formulaire = ConnexionFormulaire()
    result = render_template('index.html', connexion_formulaire=connexion_formulaire)
    if connexion_formulaire.validate_on_submit():
        Email = request.form['Email']
        Password = request.form['Password']
        users_ref = db.collection(u'Users').where(u'Email', u'==', Email)
        docs = users_ref.get()
        for doc in docs:
            test = doc.to_dict()
            if test["Password"] == f'{Password}':
                session['duree'] = time.time() + 3600  # Durée en seconde de la session
                session['Email'] = Email
                print('bv')
                result = redirect(url_for('Homepage'))
            else:
                session['Email'] = None
                result = redirect(url_for('connexion_test'))
    return result
