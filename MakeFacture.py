from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint, make_response, session
from Client import Client
from datetime import datetime
from Entreprise import Entreprise


def TakeClient(info):
    user = Client()
    user.Takeclient(info)
    post = [user.nom, user.prenom, user.mail, user.entreprise, user.telephone]
    return post


def TakeEntreprise(info):
    entreprise = Entreprise()
    entreprise.TakeEntreprise(info)
    post = [entreprise.nom, entreprise.siret, entreprise.code, entreprise.adresse, entreprise.ville]
    return post


def InfoFacture():
    date = datetime.now()
    id = str(date.strftime("%Y%m%d"))
    date = str(date.strftime("%Y-%m-%d %H:%M:%S"))
    facture = [date, id]
    return facture


def MakeFacture(Email_contact, Siret):
    user = TakeClient(Email_contact)
    facture = InfoFacture()
    entreprise = TakeEntreprise(Siret)
    return render_template('factures.html', users=user, facture=facture, entreprise = entreprise)
