from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint, make_response, session
from Client import Client
from datetime import datetime
from Entreprise import Entreprise


def takeClient(info):
    user = Client()
    user.takeClient(info)
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


def makeFacture(Email_contact, Siret):
    user = takeClient(Email_contact)
    facture = infoFacture()
    entreprise = takeEntreprise(Siret)
    return render_template('factures.html', users=user, facture=facture, entreprise = entreprise)
