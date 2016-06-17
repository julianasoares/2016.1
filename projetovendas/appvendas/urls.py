from django.conf.urls import patterns,include,url
from appvendas.views import *
urlpatterns=[
    url(r'^$',home,name='home'),
    url(r'^produtos/$',listarprodutos,name='produtos'),
    url(r'^produtos/exibir/(\d+)',exibirproduto,name='exibirproduto'),
    url(r'^unidades/$',listarunidades,name='unidades'),
    url(r'^unidades/exibir/(\d+)', exibirunidade, name='exibirunidade'),
    url(r'^vendas/$',listarvendas,name='vendas'),

]