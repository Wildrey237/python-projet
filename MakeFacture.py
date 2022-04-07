from flask import render_template
from Client import Client
from datetime import datetime
from Entreprise import Entreprise


def takeClient(info):
    user = Client()
    user.take_client(info)
    post = user
    return post


def takeEntreprise(info):
    entreprise = Entreprise()
    entreprise.take_entreprise(info)
    post = entreprise
    return post


def infoFacture():
    date = datetime.now()
    id = str(date.strftime("%Y%m%d"))
    date = str(date.strftime("%Y-%m-%d %H:%M:%S"))
    facture = [date, id]
    return facture


def make_fature(email_contact, siret):
    user = takeClient(email_contact)
    facture = infoFacture()
    entreprise = takeEntreprise(siret)
    return render_template('factures.html', users=user, facture=facture, entreprise = entreprise)


