from flask import Flask, session, redirect, request, url_for, render_template, flash
from CreateMethod import Entreprise
from connexion import connexion
from session import session_verification
from test import page_test
from makefacture import MakeFacture

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'


# Page de connexion administrateur
@app.route('/connexion', methods=['GET', 'POST'])
def connexion_test():
    return connexion()


@app.route('/test')
def test():
    return session_verification(page_test())


@app.route('/facture')
def Facture():
    return MakeFacture()


# Page d'ajout d'une entreprise dans la BDD
# @app.route('/ajout-entreprise', methods=['GET', 'POST'])
# def creation_entreprise():
#     return session_verification(Entreprise(id, Nom, Siret, Adresse, Code, Ville, Description, URL))


if __name__ == '__main__':
    app.run(debug=True)
