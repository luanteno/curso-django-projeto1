from django.urls import path

from receitas.views import contato, home, sobre

urlpatterns = [
    path('', home),  # ''(vazio) --> raiz do site
    path('sobre/', sobre),  # sobre
    path('contato/', contato),  # contato
]
