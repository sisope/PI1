
from django.urls import path
from app_controle_estoque import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # cadastro.com
    path('', views.home, name='home'),
    # cadastro.com/itens
    path('itens', views.itens, name='listagem_itens'),
]
