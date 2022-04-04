import time
from flask import session, redirect, url_for


def session_verification(maPage):
    if session['duree'] <= time.time():
        return redirect(url_for('connexion_test'))
    else:
        return maPage





