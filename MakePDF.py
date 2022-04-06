import pdfkit
from datetime import datetime


class PdfGenerator:

    def __init__(self, nom_facture: str = None):
        self.id_facture = nom_facture

    def make_PDF(self, template):
        date = datetime.now()
        id = str(date.strftime("%Y-%m-%d %H:%M:%S"))
        name = f"facture n°{id}"
        pdf = pdfkit.from_url(template, f'Facture/{name}.pdf')
        return pdf


def enregistre_PDF(email, Siret):
    template = f'http://127.0.0.1:5000/facture-{email}-{Siret}'
    fact = PdfGenerator()
    return fact.make_PDF(template)
