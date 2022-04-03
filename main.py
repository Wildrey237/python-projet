from flask import Flask, session, redirect, request, url_for, render_template, flash
from CreateMethod import createEntreprise
from connexion import connexion


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'


# Page de connexion administrateur
@app.route('/connexion', methods=['GET', 'POST'])
def connexion_test():
    return connexion()


# Page d'ajout d'une entreprise dans la BDD
@app.route('/ajout-entreprise', methods=['GET', 'POST'])
def creation_entreprise():
    return createEntreprise


if __name__ == '__main__':
    app.run(debug=True)
