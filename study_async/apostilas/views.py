from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.db.models import Q
from django.db.models import Sum
from .models import Apostila, ViewApostila, Avaliacao


def adicionar_apostilas(request):
    if not request.user.is_authenticated:
        login_url = reverse('login')  # Certifique-se de que 'login' é o nome da sua URL de login
        return redirect(login_url)

    if request.method == 'GET':
        apostilas = Apostila.objects.filter()
        # TODO: feito Criar as tags

        views_totais = ViewApostila.objects.filter(
                apostila__in=apostilas
            ).count() or 0

        return render(
            request,
            'apostilas/adicionar_apostilas.html',
            {'apostilas': apostilas,'views_totais': views_totais},
        )

    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        arquivo = request.FILES.get('arquivo')
        tags = request.POST.get('tags')

        error=False
        if not titulo:
            error=True
            messages.error(request, 'Informe o título da apostila.')

        if not arquivo:
            error=True
            messages.error(request, 'Selecione e envie o arquivo referente a apostila.')

        if not tags:
            error=True
            messages.error(request, 'Informe alguma tag de busca para indexar ao arquivo da apostila.')

        if  not error:
            apostila = Apostila(user=request.user, titulo=titulo, arquivo=arquivo, tags=tags)
            apostila.save()
            messages.add_message(
                request, constants.SUCCESS, 'Apostila adicionada com sucesso.'
            )

        return redirect('/apostilas/adicionar_apostilas/')

def apostila(request, id):
    if not request.user.is_authenticated:
        login_url = reverse('login')  # Certifique-se de que 'login' é o nome da sua URL de login
        return redirect(login_url)

    apostila = Apostila.objects.get(id=id)

    view = ViewApostila(ip=request.META['REMOTE_ADDR'], apostila=apostila)
    view.save()

    views_unicas = (
        ViewApostila.objects.filter(apostila=apostila)
        .values('ip')
        .distinct()
        .count() or 0
    )

    views_totais = ViewApostila.objects.filter(
        apostila=apostila
    ).count() or 0

    # Obtendo as médias de avaliação
    media_ruim = apostila.media_avaliacoes(Avaliacao.RUIM)
    media_bom = apostila.media_avaliacoes(Avaliacao.BOM)
    media_otimo = apostila.media_avaliacoes(Avaliacao.OTIMO)
    media_excelente = apostila.media_avaliacoes(Avaliacao.EXCELENTE)
    escolhas_avaliacao = Avaliacao.ESCOLHAS_AVALIACAO

    user = request.user
    avaliacaoSelecionada = Avaliacao.objects.filter(apostila=apostila, usuario=user).first()
    if Avaliacao.objects.filter(apostila=apostila, usuario=user).exists():
        avaliacaoUser = avaliacaoSelecionada.avaliacao
        avaliacaoSelecionada = avaliacaoUser
    else:
        avaliacaoSelecionada = None



    return render(
        request,
        'apostilas/apostila.html',
        {
            'apostila': apostila,
            'views_unicas': views_unicas,
            'views_totais': views_totais,
            'escolhas_avaliacao' : escolhas_avaliacao,
            'media_ruim': media_ruim,
            'media_bom': media_bom,
            'media_otimo': media_otimo,
            'media_excelente': media_excelente,
            'avaliacaoSelecionada':avaliacaoSelecionada,
        },
    )

def buscar_apostilas(request):
    if not request.user.is_authenticated:
        login_url = reverse('login')  # Certifique-se de que 'login' é o nome da sua URL de login
        return redirect(login_url)

    if request.method == 'GET':
        tags = tags = request.GET.get('tags', '')
        tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]

        # Construir as condições OR usando Q
        query_conditions = Q()
        for tag in tag_list:
            query_conditions |= Q(tags__icontains=tag)

        # Consulta final
        apostilas = Apostila.objects.filter(query_conditions)


        views_totais = ViewApostila.objects.filter(
                apostila__in=apostilas
            ).count() or 0



        return render(
            request,
            'apostilas/adicionar_apostilas.html',
            {'apostilas': apostilas,'views_totais': views_totais,'tagsBuscadas':tags},
        )

def avaliar_apostila(request, id):
    if not request.user.is_authenticated:
        login_url = reverse('login')  # Certifique-se de que 'login' é o nome da sua URL de login
        return redirect(login_url)

    apostila = get_object_or_404(Apostila, id=id)
    escolhas_avaliacao = Avaliacao.ESCOLHAS_AVALIACAO

    if request.method == 'POST':
        avaliacao = request.POST.get('avaliacao')
        user = request.user

        if Avaliacao.objects.filter(apostila=apostila, usuario=user).exists():
            avaliacaoUpdateUser = Avaliacao.objects.filter(apostila=apostila, usuario=user).first()
            avaliacaoUpdateUser.avaliacao = avaliacao
            avaliacaoUpdateUser.save()
            messages.success(request, 'Avaliação atualizada com sucesso.')
        else:
            Avaliacao.objects.create(apostila=apostila, usuario=user, avaliacao=avaliacao)
            messages.success(request, 'Avaliação adicionada com sucesso.')

        return HttpResponseRedirect(reverse('apostila', args=[apostila.id]))

    # Obtendo as médias de avaliação
    media_ruim = apostila.media_avaliacoes(Avaliacao.RUIM)
    media_bom = apostila.media_avaliacoes(Avaliacao.BOM)
    media_otimo = apostila.media_avaliacoes(Avaliacao.OTIMO)
    media_excelente = apostila.media_avaliacoes(Avaliacao.EXCELENTE)

    views_unicas = (
        ViewApostila.objects.filter(apostila=apostila)
        .values('ip')
        .distinct()
        .count()
    )

    views_totais = ViewApostila.objects.filter(
        apostila=apostila
    ).count()

    user = request.user
    avaliacaoSelecionada = Avaliacao.objects.filter(apostila=apostila, usuario=user).first()
    if Avaliacao.objects.filter(apostila=apostila, usuario=user).exists():
        avaliacaoUser = avaliacaoSelecionada.avaliacao
        avaliacaoSelecionada = avaliacaoUser
    else:
        avaliacaoSelecionada = None

    return render(
        request,
        'apostilas/apostila.html',
        {
            'apostila': apostila,
            'views_unicas': views_unicas,
            'views_totais': views_totais,
            'escolhas_avaliacao' : escolhas_avaliacao,
            'media_ruim': media_ruim,
            'media_bom': media_bom,
            'media_otimo': media_otimo,
            'media_excelente': media_excelente,
            'avaliacaoSelecionada':avaliacaoSelecionada
        },
    )