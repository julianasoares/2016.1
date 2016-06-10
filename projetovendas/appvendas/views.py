from django.shortcuts import render
from django.http import HttpResponse
from appvendas.models import *
# Create your views here.

def produtos(request):
    produtos=Produto.objects.all().order_by('descricao')
    lista={'produtos':produtos}
    return render(request,'produtos.html',lista)
def unidades(request):
    unidades=Unidade.objects.all().order_by('descricao')
    lista={'unidades':unidades}
    return render(request,'unidades.html',lista)
