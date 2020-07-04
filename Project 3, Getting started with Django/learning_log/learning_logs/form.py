from django import forms
from .models import Topic
from .models import Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text'] #che tipo di dati accettiamo per il modello
        labels = {'text': ''} #non generare una label per i campi di testo

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text' : forms.Textarea(attrs={'cols': 80})} #80 colonnne invece che le 40 di default
