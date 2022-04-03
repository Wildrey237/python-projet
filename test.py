from flask import render_template

from connexion import db


def page_test():
    client_ref = db.collection(u'Client')
    result = client_ref.get()
    t2 = []
    for r in result:
        testt = r.to_dict()
        t2.append(testt)
    return render_template('test.html', liste_client=t2)
