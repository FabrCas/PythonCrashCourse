from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse # per determinare l'URL da un certo pattern URL


from .models import Topic
from .form import TopicForm
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

def new_topic(request):
    print("********************************************************+view new_topic ")
    if request.method !='POST':  #quindi get, creazione della pagina per la sola lettura -> get, invia le info -> post
        # dati non inviati, crea una form vuota
        form= TopicForm()
    else:
        # dati inviati, processali
        form = TopicForm(request.POST)  #request.POST è un dictionary like che contiene tutte le informazioni necessarie per la form
        if form.is_valid():
            form.save()   #salva sul db
            return HttpResponseRedirect(reverse("learning_logs:topics"))
    context= {'form': form}
    return render(request, 'new_topic.html', context)

