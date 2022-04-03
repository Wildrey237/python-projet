from flask import redirect, request, url_for, render_template
from formulaires import ConnexionFormulaire
from CONNECTdb import connect_BD

db = connect_BD()

def connexion():
    connexion_formulaire = ConnexionFormulaire()
    if connexion_formulaire.validate_on_submit():
        Email = request.form['Email']
        Password = request.form['Password']
        users_ref = db.collection(u'Users').where(u'Email', u'==', Email)
        docs = users_ref.get()
        for doc in docs:
            test = doc.to_dict()
            if test["Password"] == f'{Password}':
                print('bv')
            else:
                return redirect(url_for('connexion_test'))
    return render_template('connexion.html', connexion_formulaire=connexion_formulaire)
