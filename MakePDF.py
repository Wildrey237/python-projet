import pdfkit
from datetime import datetime
from Connexion import db
from flask import redirect


class PdfGenerator:

    def __init__(self, id_facture: str = None, date=None, email: str = None, SiretEntreprise: int = None):
        self.id_facture = id_facture
        self.date = date
        self.email = email
        self.SiretEntreprise = SiretEntreprise

    def make_PDF(self, template):
        self.date = datetime.now()
        id = str(self.date.strftime("%Y-%m-%d %H:%M:%S"))
        self.id_facture = f"facture n°{id}"
        pdf = pdfkit.from_url(template, f'Facture/{self.id_facture}.pdf')
        return pdf

    def take(self, email, siret):
        self.email = email
        self.SiretEntreprise = siret
        return self.email, self.SiretEntreprise

    def save(self):
        date = datetime.now()
        db.collection('Facture').add(
            {
                'Date': date,
                'Facture n°': str(date.strftime("%Y-%m-%d %H:%M:%S")),
                'SiretEntreprise': self.SiretEntreprise,
                'Mail': self.email
            }
        )


def enregistre_PDF(email, Siret):
    fact = PdfGenerator()
    fact.take(email, Siret)
    fact.save()
    template = f'http://127.0.0.1:5000/facture-{email}-{Siret}'
    return fact.make_PDF(template)


def facture_final(email, Siret):
    enregistre_PDF(email, Siret)
    return redirect(f'/facture-{email}-{Siret}')
