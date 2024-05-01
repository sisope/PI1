from django.shortcuts import render
from .models import Item


def home(request):
    return render(request, 'cadastro/home.html')


def itens(request):
    # Salvar os dados da tela para o Banco de Dados
    novo_item = Item()
    novo_item.nome = request.POST.get('nome')
    novo_item.quantidade = request.POST.get('quantidade')
    novo_item.save()

    # Exibir todos os novos itens em uma nova página
    itens = {
        'itens': Item.objects.all()
    }
    # Retornar os dados para a página de listagem de itens
    return render(request, 'cadastro/itens.html', itens)
