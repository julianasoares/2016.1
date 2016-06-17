from django.shortcuts import render
from django.http import HttpResponse
from appvendas.models import *
# Create your views here.

def home(request):
    return render(request,'base.html')
def exibirproduto(request,id_produto):
    produto=Produto.objects.get(id=id_produto)
    return render(request,'exibirproduto.html',{'produto':produto})
def listarprodutos(request):
    produtos=Produto.objects.all().order_by('descricao')
    lista={'produtos':produtos}
    return render(request,'produtos.html',lista)
def listarunidades(request):
    unidades=Unidade.objects.all().order_by('descricao')
    lista={'unidades':unidades}
    return render(request,'unidades.html',lista)
def exibirunidade(request,id_unidade):
    unidade=Unidade.objects.get(id=id_unidade)
    return render(request,'exibirunidade.html',{'unidade':unidade})
def listarvendas(request):
    vendas=Venda.objects.all()
    lista={'vendas':vendas}
    return render(request,'vendas.html',lista)