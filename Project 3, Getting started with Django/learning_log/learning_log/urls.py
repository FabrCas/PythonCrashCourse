"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs')), #app_name='learning_logs', secondo parametro nella tupla
    #abbiamo incluso il modulo learning_logs.urls in modo da distingure gli URL del nostro applicativo dagli altri che
    #possono esistere nel progetto, url è un alias della funzione re_path(...)
]


