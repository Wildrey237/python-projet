from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint, make_response, session
from Client import Client
from datetime import datetime


def TakeClient(info):
    user = Client()
    user.Takeclient(info)
    post = [user.nom, user.prenom, user.mail, user.entreprise, user.telephone]
    return post


def InfoFacture():
    date = datetime.now()
    date = str(date.strftime("%Y-%m-%d %H:%M:%S"))
    facture = [date]
    return facture


def MakeFacture():
    user = TakeClient('erwann.duclos@epsi.fr')
    facture = InfoFacture()
    return render_template('factures.html', users=user, facture=facture)
