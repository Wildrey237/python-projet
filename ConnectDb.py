import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def connect_BD():
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
    database = firestore.client()
    return database
