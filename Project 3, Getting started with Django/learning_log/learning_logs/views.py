from django.shortcuts import render
from .models import Topic
# Create your views here.

def index(request):
    """ la home page del sito"""
    return render(request, 'index.html')  #in settings.py è stato impostato il path di default per i templates a cui verrà
                                          #aggiunto il nome del file html specificato nei parametri passati alla funzione render
def topics(request):
    """ mostra tutti i topics"""
    topics = Topic.objects.order_by("date_added")
    context = {'topics': topics}
    return  render(request, 'topics.html', context)

def topic(request, topic_id):
    topic= Topic.objects.get(id=topic_id)
    entries= topic.entry_set.order_by('-date_added')
    context= {'topic': topic, 'entries': entries}
    return  render(request, 'topic.html', context)