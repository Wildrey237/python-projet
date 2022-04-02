from flask import Flask, session, redirect, request, url_for, render_template, flash
from connexion import connexion
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'


@app.route('/connexion', methods=['GET', 'POST'])
def connexion_test():
    return connexion()


if __name__ == '__main__':
    app.run(debug=True)


