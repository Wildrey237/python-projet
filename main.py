import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask

from Entreprise import makeEntreprise, modifyEntreprise
from Connexion import connexion
from Client import makeClient
from Session import session_verification
from Test import page_test
from MakeFacture import makeFacture

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'


# Page de connexion administrateur
@app.route('/', methods=['GET', 'POST'])
def connexion_test():
    return connexion()


# Page de test pour les variables de sessions de 60 minutes
@app.route('/test', methods=['GET', 'POST'])
def test():
    return session_verification(page_test())


# Page d'ajout d'une entreprise dans la BDD
@app.route('/ajout-entreprise', methods=['GET', 'POST'])
def ajoutEntreprise():
    return session_verification(makeEntreprise())


@app.route('/Entreprise/<siret>')
def entreprise(siret):
    return session_verification(modifyEntreprise(siret))


# Page d'ajout d'un client dans la BDD
@app.route('/ajout-client', methods=['GET', 'POST'])
def ajoutClient():
    return session_verification(makeClient())


@app.route('/facture', methods=['GET', 'POST'])
def Facture():
    Email_contact = "hello"
    Siret = 1
    return makeFacture(Email_contact, Siret)


if __name__ == '__main__':
    app.run(debug=True)
