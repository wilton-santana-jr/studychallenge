from django.urls import path

from . import views

urlpatterns = [
    path(
        'adicionar_apostilas/',
        views.adicionar_apostilas,
        name='adicionar_apostilas',
    ),
     path(
        'buscar_apostilas/',
        views.buscar_apostilas,
        name='buscar_apostilas',
    ),
     path(
        'avaliar_apostila/<int:id>',
        views.avaliar_apostila,
        name='avaliar_apostila',
    )
    ,
    path('apostila/<int:id>', views.apostila, name='apostila'),
]
