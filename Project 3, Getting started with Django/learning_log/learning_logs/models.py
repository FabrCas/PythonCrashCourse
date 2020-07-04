from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic (models.Model): #sottoclasse di Model
    # un argomento che l'utente potrà leggere
    text= models.CharField(max_length= 200)
    date_added= models.DateTimeField(auto_now_add= True)
    owner= models.ForeignKey(User, default= 1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.text

class Entry(models.Model):
    """ descrizione di un argomento (Topic), relazione many to one con essa """
    topic= models.ForeignKey(Topic, on_delete=models.CASCADE)  #id dei topics
    text= models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    """Meta contiene informazioni supplementari per la gestione dei modelli"""
    class Meta:
        verbose_name_plural= "entries" #entries invece di entrys

        def __str__(self):
            return self.text[:50] + "..." #ritorna i primi 50 caratteri

