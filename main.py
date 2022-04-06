from flask import Flask

from Client import make_client, modify_client
from Commentaire import make_commentaire
from Connexion import connexion
from Entreprise import make_entreprise, modify_entreprise
from MakeFacture import make_fature
from Session import session_verification
from Homepage import page_test
from MakePDF import facture_final

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'


# Page de connexion administrateur
@app.route('/', methods=['GET', 'POST'])
def connexion_test():
    return connexion()


# Page de test pour les variables de sessions de 60 minutes
@app.route('/Homepage', methods=['GET', 'POST'])
def Homepage():
    return session_verification(page_test())

@app.route('/Client-<Email>', methods=['GET', 'POST'])
def client(Email):
    return session_verification(modify_client(Email))


# Page d'ajout d'une entreprise dans la BDD
@app.route('/ajout-entreprise', methods=['GET', 'POST'])
def ajoutEntreprise():
    return session_verification(make_entreprise())


@app.route('/Entreprise-<siret>', methods=['GET', 'POST'])
def entreprise(siret):
    return session_verification(modify_entreprise(siret))


# Page d'ajout d'un client dans la BDD
@app.route('/ajout-client', methods=['GET', 'POST'])
def ajoutClient():
    return session_verification(make_client())


# Page d'ajout de commentaire sur un client (personne physique) existant
@app.route('/ajout-commentaire-<telephone>', methods=['GET', 'POST'])
def ajoutCommentaire(telephone):
    return session_verification(make_commentaire(telephone))


@app.route('/facture-<Email_contact>-<Siret>', methods=['GET', 'POST'])
def Facture(Email_contact, Siret):
    Siret_int = float(Siret)
    return make_fature(Email_contact, Siret_int)

@app.route('/pdf-<Email_contact>-<Siret>', methods=['GET', 'POST'])
def pdf(Email_contact, Siret):
    Siret_int = float(Siret)
    return facture_final(Email_contact, Siret_int)


if __name__ == '__main__':
    app.run(debug=True)
