from flask import render_template, request
from formulaires import FormulaireCreationEntreprise
from connexion import db


# Create data in db - cette méthode ajoute une entreprise
def createEntreprise():
    creation_entreprise = FormulaireCreationEntreprise
    if creation_entreprise.validate_on_submit():
        Nom = request.form['Nom']
        Siret = request.form['Siret']
        Adresse = request.form['Adresse']
        Code = request.form['Code']
        Ville = request.form['Ville']
        Description = request.form['Description']
        URl = request.form['URL']
        query = db.collection('Entreprise').add(
            {
                'Nom': Nom,
                'Siret': Siret,
                'Adresse': Adresse,
                'Code': Code,
                'Ville': Ville,
                'Description': Description,
                'URL': URl
            }
        )
        print(query)
    return render_template('creationEntreprise.html', creation_entreprise=creation_entreprise)

# Create data in db - cette méthode fonctionne pour ajouter un client
# def createClient():
#     db.collection('Client').add(
#         {
#             'Prenom': 'Erwann',
#             'Nom': 'Duclos',
#             'Email': 'erwann.duclos@epsi.fr',
#             'Poste': 'Enseignant',
#             'Telephone': '0642934669',
#             'Statut': True
#         }
#     )
#
#
# '''createClient()'''

# Create data in db - cette méthode fonctionne pour ajouter un admin
# def createUser():
#     db.collection('Users').add(
#         {
#             'Email': 'anthony.meny@gmail.com',
#             'Password': 'SecretPassword'
#         }
#     )
#
#
# '''createUser()'''


# Create data in db - Permet d'ajouter une facture avec la temporalité #TODO ajouter l'autoincrémentation du numéro de facture
# def createFacture():
#     db.collection('Facture').add(
#         {
#             'Date': datetime.datetime.now(),
#             'Emetteur': 'EPSI',
#             'Receveur': 'Anthony',
#         }
#     )
#
#
# '''createFacture()'''


# def createComm():
#     db.collection('Commentaire').add(
#         {
#             'Auteur': '',
#             'Date de création': datetime.datetime.now(),
#             'Description': ''
#         }
#     )
#
#
# createComm()


# UPDATE date in db - avec une key unknown (qui est hash)

# 1ere méthode
# docs = db.collection('Client').get()  # Read TOUTE la data de 'Client'
# for doc in docs:
#     if doc.to_dict()['#age'] >= 20:
#         key = doc.id
#         db.collection('Client').document(key).update({"Agegroupe": "Adulte"})

# 2ème méthode
# docs = db.collection('Client').where("age", ">=", 50).get()  # Read la data qui respecte la condition
# for doc in docs:
#     key = doc.id
#     db.collection('Client').document(key).update({"Agegroupe": "Plus vieux que 50 ans"})


# def modify():
#     docs = db.collection('Client').where("Nom", "==", ).get()  # Read la data qui respecte la condition
#     for doc in docs:
#         key = doc.id
#         db.collection('Client').document(key).set({"Nom": "Test"})
#
#
# '''modify()'''
#
#
# # DELETE data in db -
#
#
# def delete():
#     pass
