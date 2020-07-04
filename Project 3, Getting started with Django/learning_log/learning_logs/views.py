from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse # per determinare l'URL da un certo pattern URL


from .models import Topic, Entry
from .form import TopicForm, EntryForm
# Create your views here.

def index(request):
    """ la home page del sito"""
    return render(request, 'index.html')  #in settings.py è stato impostato il path di default per i templates a cui verrà
                                        #aggiunto il nome del file html specificato nei parametri passati alla funzione render
@login_required
def topics(request):
    """ mostra tutti i topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return  render(request, 'topics.html', context)

@login_required
def topic(request, topic_id):
    topic= Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries= topic.entry_set.order_by('-date_added')
    context= {'topic': topic, 'entries': entries}
    return  render(request, 'topic.html', context)

@login_required
def new_topic(request):
    if request.method !='POST':  #quindi get, creazione della pagina per la sola lettura -> get, invia le info -> post
        # dati non inviati, crea una form vuota
        form= TopicForm()
    else:
        # dati inviati, processali
        form = TopicForm(request.POST)  #request.POST è un dictionary like che contiene tutte le informazioni necessarie per la form
        if form.is_valid():
            new_topic= form.save(commit= False)
            new_topic.owner = request.user
            new_topic.save()
            form.save()   #salva sul db
            return HttpResponseRedirect(reverse("learning_logs:topics"))
    context= {'form': form}
    return render(request, 'new_topic.html', context)\

@login_required
def new_entry(request,topic_id):
    print(topic_id)
    topic = Topic.objects.get(id=topic_id)
    if request.method !='POST':
        form= EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry= form.save(commit=False)  #prende la entry con i dati inseriti dalla form
            new_entry.topic = topic   #gli assegno un topic
            new_entry.save()
            return HttpResponseRedirect(reverse("learning_logs:topic", args=[topic_id]))
    context= {'topic': topic,'form': form}
    return render(request, 'new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry= Entry.objects.get(id=entry_id)
    topic= entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != "POST":
        form = EntryForm()
    else:
        form= EntryForm(instance= entry, data= request.POST) #request.POST serve per indicare a Django di creare un form sui sui dati inseriti
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("learning_logs:topic", args=[topic.id]))
    context={'entry':entry,'topic':topic, 'form': form}
    return render(request, 'edit_entry.html', context)


