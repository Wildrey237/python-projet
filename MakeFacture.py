from flask import render_template
from Client import Client
from datetime import datetime
from Entreprise import Entreprise


def take_client(info):
    user = Client()
    user.take_client(info)
    post = user
    return post


def take_entreprise(info):
    entreprise = Entreprise()
    entreprise.take_entreprise(info)
    post = entreprise
    return post


def info_facture():
    date = datetime.now()
    id = str(date.strftime("%Y%m%d"))
    date = str(date.strftime("%Y-%m-%d %H:%M:%S"))
    facture = [date, id]
    return facture


def make_facture(email_contact, siret):
    user = take_client(email_contact)
    facture = info_facture()
    entreprise = take_entreprise(siret)
    return render_template('factures.html', users=user, facture=facture, entreprise = entreprise)


