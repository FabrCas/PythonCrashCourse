"""defineremo qui gli URLs per il progetto learning_logs"""

from django.conf.urls import url
from . import  views # il dot, indica di importare da la stessa cartella del file urls.py in learning_logs

urlpatterns = [
    # Reindirizzamento alla home page
    url(r'^$', views.index, name='index'), #con r indichiamo l'utilizzo di una raw string, in questo caso la stringa vuota di
    #default è l'indirizzo URL base 127.0.0.1 o http://localhost:8000/
    url(r'^topics/$', views.topics, name="topics"), #url per la pagina con le liste di topics
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name="topic"), #? indica l'inizio della query, \d+ indica di catturare ogni numero digitat
    # tra le slash, P<topic_id> serve a salvare il parametro in topic_id
    url(r'^new_topic/$', views.new_topic, name="new_topic")
]