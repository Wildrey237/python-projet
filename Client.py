from CONNECTdb import connect_BD

class Client:
    def Takeclient(self, Email: str = None):
        db = connect_BD()
        if Email is None:
            docs = db.collection('Client')
        else:
            docs = db.collection('Client').where(u'Email', u'==', Email)
        docs = docs.get()
        user = []
        for doc in docs:
            post = doc.to_dict()
            user.append(post)
        user = user[0]
        self.mail = user["Email"]
        """self.entreprise = user["Entreprise"]"""
        self.nom = user["Nom"]
        self.prenom = user["Prenom"]
        self.poste = user["Poste"]
        self.statut = user["Statut"]
        self.telephone = user["Telephone"]

    def __init__(self, mail: str = None, Entreprise: str = None, Nom: str = None, Poste: bool = True,
                 Prenom: str = None, Statut: str = None, Telephone: int = None):
        self.mail = mail
        self.entreprise = Entreprise
        self.nom = Nom
        self.prenom = Prenom
        self.poste = Poste
        self.statut = Statut
        self.telephone = Telephone