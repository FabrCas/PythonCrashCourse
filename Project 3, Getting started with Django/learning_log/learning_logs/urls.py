"""defineremo qui gli URLs per il progetto learning_logs"""

from django.conf.urls import url
from . import  views # il dot, indica di importare da la stessa cartella del file urls.py in learning_logs

urlpatterns = [
    # Reindirizzamento alla home page
    url(r'^$', views.index, name='index') #con r indichiamo l'utilizzo di una regex, in questo caso la stringa vuota di
    #default è l'indirizzo URL base 127.0.0.1 o http://localhost:8000/
]