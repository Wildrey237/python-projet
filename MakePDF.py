import pdfkit
from datetime import datetime

template = 'http://127.0.0.1:5000/facture'


class PdfGenerator:

    def __init__(self, nom_facture: str = None):
        self.id_facture = nom_facture

    def make_PDF(self):
        date = datetime.now()
        id = str(date.strftime("%Y-%m-%d %H:%M:%S"))
        name = f"facture n°{id}"
        pdf = pdfkit.from_url(template, f'Facture/{name}.pdf')
        return pdf


fact = PdfGenerator()
fact.make_PDF()
