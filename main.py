from flask import Flask

from CreateMethod import *
from connexion import connexion
from session import session_verification
from test import page_test

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
    return session_verification(makeEntreprise)


if __name__ == '__main__':
    app.run(debug=True)
