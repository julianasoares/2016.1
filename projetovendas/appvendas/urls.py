from django.conf.urls import patterns,include,url
from appvendas.views import *
urlpatterns=[
    url(r'^produtos/$',produtos,name='produtos'),
    url(r'^unidades/$',unidades,name='unidades'),
]