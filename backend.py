from service.models import signup
from django.contrib.sessions.backends.db import SessionStore

def logins(request,data):  
    session=SessionStore()
    session["username"]=data[0]["Email"]
    session.save()
    request.session=session

def logouts(request):
    request.session.flush()