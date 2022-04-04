import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask

from Entreprise import makeEntreprise
from Connexion import connexion
from Client import makeClient
from Session import session_verification
from Test import page_test
from MakeFacture import MakeFacture

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'


# Page de connexion administrateur
@app.route('/connexion', methods=['GET', 'POST'])
def connexion_test():
    return connexion()


# Page de test pour les variables de sessions de 60 minutes
@app.route('/test')
def test():
    return session_verification(page_test())


# Page d'ajout d'une entreprise dans la BDD
@app.route('/ajout-entreprise', methods=['GET', 'POST'])
def ajoutEntreprise():
    return session_verification(makeEntreprise())


# Page d'ajout d'un client dans la BDD
@app.route('/ajout-client', methods=['GET', 'POST'])
def ajoutClient():
    return session_verification(makeClient())


@app.route('/facture/<Email>', methods=['GET', 'POST'])
def Facture(Email):
    return MakeFacture(Email)


if __name__ == '__main__':
    app.run(debug=True)
