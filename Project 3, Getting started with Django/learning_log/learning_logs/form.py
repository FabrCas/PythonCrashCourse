from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text'] #che tipo di dati accettiamo per il modello
        labels = {'text': ''} #non generare una label per i campi di testo

