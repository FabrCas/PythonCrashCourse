from django.db import models

# Create your models here.

class Topic (models.Model): #sottoclasse di Model
    # un argomento che l'utente potrà leggere
    text= models.CharField(max_length= 200)
    date_added= models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.text

    

