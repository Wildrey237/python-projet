from formulaires import ConnexionFormulaire
from flask import Flask, session, redirect, request, url_for, render_template, flash
import firebase_admin
from firebase_admin import credentials, firestore


def connexion():
    connexion_formulaire = ConnexionFormulaire()
    db = firestore.client()
    if connexion_formulaire.validate_on_submit():
        email = request.form['email']
        mdp = request.form['mdp']
        users_ref = db.collection(u'test').where(u'nom', u'==', email)
        docs = users_ref.get()
        for doc in docs:
            test = doc.to_dict()
        if test["mdp"] == f'{mdp}':
            print('bv')
        else:
            return redirect(url_for('connexion_test'))
    return render_template('connexion.html', connexion_formulaire=connexion_formulaire)



