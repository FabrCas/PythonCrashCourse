from django.shortcuts import render

# Create your views here.

def index(request):
    """ la home page del sito"""
    return render(request, 'learning_logs/index.html')
