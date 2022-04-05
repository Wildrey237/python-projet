import pdfkit
from datetime import datetime


class PDFGenerator:

    def __init__(self, nom_facture: str = None):
        self.id_facture = nom_facture

    def Make_PDF(self, template):
        date = datetime.now()
        id = str(date.strftime("%Y-%m-%d %H:%M:%S"))
        name = f"facture n°{id}"
        pdf = pdfkit.from_url(template, f'Facture/{name}.pdf')
        return pdf


fact = PDFGenerator()
fact.Make_PDF('https://www.reddit.com/')
