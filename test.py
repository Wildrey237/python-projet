from flask import render_template
import firebase_admin
from firebase_admin import credentials, firestore

def page_test():
    db = firestore.client()
    client_ref = db.collection(u'Client')
    result = client_ref.get()
    t2 = []
    for r in result:
        testt = r.to_dict()
        t2.append(testt)
    return render_template('test.html', liste_client=t2)
