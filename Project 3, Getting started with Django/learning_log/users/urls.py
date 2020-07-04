from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns= [
    # login page
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name= 'login'),
    # siccome non abbiamo creato la nostra funzione vista, dobbiamo passargli un dictionary con le info per la posizione
    # del template
    url(r'^logout/$', views.logout_view, name='logout'),
]