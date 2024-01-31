from django.contrib import messages
from django.contrib.messages import constants
from django.http import Http404
from django.shortcuts import redirect, render

from .models import Categoria, Desafio, Flashcard, FlashcardDesafio


def novo_flashcard(request):
    if not request.user.is_authenticated:
        return redirect('usuarios/login')

    if request.method == 'GET':
        categorias = Categoria.objects.all()
        dificuldades = Flashcard.DIFICULDADE_CHOICES
        flashcards = Flashcard.objects.filter(user=request.user)

        categoria_filtrar = request.GET.get('categoria')
        dificuldade_filtrar = request.GET.get('dificuldade')

        if categoria_filtrar:
            flashcards = flashcards.filter(categoria__id=categoria_filtrar)            
            categoria_filtrar = int(categoria_filtrar)

        if dificuldade_filtrar:
            flashcards = flashcards.filter(dificuldade=dificuldade_filtrar)

        return render(
            request,
            'flashcard/novo_flashcard.html',
            {
                'categoriaSelecionada': categoria_filtrar,
                'dificuldadeSelecionada': dificuldade_filtrar,
                'categorias': categorias,
                'dificuldades': dificuldades,
                'flashcards': flashcards,
            },
        )
    elif request.method == 'POST':
        pergunta = request.POST.get('pergunta')
        resposta = request.POST.get('resposta')
        categoria = request.POST.get('categoria')
        dificuldade = request.POST.get('dificuldade')

        if len(pergunta.strip()) == 0 or len(resposta.strip()) == 0:
            messages.add_message(
                request,
                constants.ERROR,
                'Preencha os campos de pergunta e resposta',
            )
            return redirect('novo_flashcard')

        flashcard = Flashcard(
            user=request.user,
            pergunta=pergunta,
            resposta=resposta,
            categoria_id=categoria,
            dificuldade=dificuldade,
        )

        flashcard.save()

        messages.add_message(
            request, constants.SUCCESS, 'Flashcard criado com sucesso'
        )
        return redirect('novo_flashcard')


def deletar_flashcard(request, id):
    flashcard = Flashcard.objects.get(id=id)

    if not flashcard.user == request.user:
        messages.add_message(
            request,
            constants.ERROR,
            'Esse Flashcard não é seu',
        )
        return redirect('/flashcard/novo_desafios/')

    Flashcard.objects.filter(user=request.user)
    flashcard.delete()
    messages.add_message(
        request, constants.SUCCESS, 'Flashcard deletado com sucesso!'
    )
    return redirect('novo_flashcard')


def iniciar_desafio(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        dificuldades = Flashcard.DIFICULDADE_CHOICES
        return render(
            request,
            'flashcard/iniciar_desafio.html',
            {'categorias': categorias, 'dificuldades': dificuldades},
        )
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        categorias = request.POST.getlist('categoria')
        dificuldade = request.POST.get('dificuldade')
        qtd_perguntas = request.POST.get('qtd_perguntas')

        desafio = Desafio(
            user=request.user,
            titulo=titulo,
            quantidade_perguntas=qtd_perguntas,
            dificuldade=dificuldade,
            status='A'
        )
        

        desafio.categoria.add(*categorias)

        flashcards = (
            Flashcard.objects.filter(user=request.user)
            .filter(dificuldade=dificuldade)
            .filter(categoria_id__in=categorias)
            .order_by('?')
        )

        if flashcards.count() < int(qtd_perguntas):
            return redirect('/flashcard/iniciar_desafio/')

        flashcards = flashcards[: int(qtd_perguntas)]

        for f in flashcards:
            flashcard_desafio = FlashcardDesafio(
                flashcard=f,
            )
            flashcard_desafio.save()
            desafio.flashcards.add(flashcard_desafio)

        desafio.save()

        # return redirect(f'/flashcard/desafio/{desafio.id}')
        return redirect(f'/flashcard/listar_desafio')


def listar_desafio(request):
    desafios = Desafio.objects.filter(user=request.user)
    # TODO: Desenvolver os status feito
    # TODO: Desenvolver os filtros feito

    categorias = Categoria.objects.all()
    dificuldades = Flashcard.DIFICULDADE_CHOICES
    status = Desafio.STATUS_CHOICES

    categoria_filtrar = request.GET.get('categoria')
    dificuldade_filtrar = request.GET.get('dificuldade')
    status_filtrar = request.GET.get('status')

    if categoria_filtrar:
        desafios = desafios.filter(categoria__id=categoria_filtrar)            
        categoria_filtrar = int(categoria_filtrar)

    if dificuldade_filtrar:
        desafios = desafios.filter(dificuldade=dificuldade_filtrar)

    if status_filtrar:
        desafios = desafios.filter(status=status_filtrar)


    return render(
        request,
        'flashcard/listar_desafio.html',
        {
            'desafios': desafios,
            'categoriaSelecionada': categoria_filtrar,
            'dificuldadeSelecionada': dificuldade_filtrar,
            'statusSelecionado': status_filtrar,
            'categorias': categorias,
            'dificuldades': dificuldades,
            'statusList': status,
        },
    )


def desafio(request, id):
    desafio = Desafio.objects.get(id=id)

    if not desafio.user == request.user:
        raise Http404()

    if request.method == 'GET':
        acertos = (
            desafio.flashcards.filter(respondido=True)
            .filter(acertou=True)
            .count()
        )
        erros = (
            desafio.flashcards.filter(respondido=True)
            .filter(acertou=False)
            .count()
        )
        faltantes = desafio.flashcards.filter(respondido=False).count()

        if(faltantes == 0):
            desafio.status='F' #DESAFIO FINALIZADO
            desafio.save()



        return render(
            request,
            'flashcard/desafio.html',
            {
                'desafio': desafio,
                'acertos': acertos,
                'erros': erros,
                'faltantes': faltantes,
            },
        )


def responder_flashcard(request, id):
    flashcard_desafio = FlashcardDesafio.objects.get(id=id)

    acertou = request.GET.get('acertou')
    desafio_id = request.GET.get('desafio_id')

    if not flashcard_desafio.flashcard.user == request.user:
        raise Http404()

    flashcard_desafio.respondido = True
    flashcard_desafio.acertou = True if acertou == '1' else False
    flashcard_desafio.save()

    return redirect(f'/flashcard/desafio/{desafio_id}/')


def relatorio(request, id):
    desafio = Desafio.objects.get(id=id)

    return render(request, 'relatorio.html', {'desafio': desafio})


def relatorio(request, id):
    desafio = Desafio.objects.get(id=id)

    acertos = desafio.flashcards.filter(acertou=True).count()
    erros = desafio.flashcards.filter(acertou=False).count()

    dados = [acertos, erros]

    categorias = desafio.categoria.all()
    name_categoria = [i.nome for i in categorias]

    dados2 = []
    for categoria in categorias:
        dados2.append(
            desafio.flashcards.filter(flashcard__categoria=categoria)
            .filter(acertou=True)
            .count()
        )


    # Dados de acertos e erros por categoria
    dados_categorias = []
    for categoria in categorias:
        acertos_categoria = desafio.flashcards.filter(flashcard__categoria=categoria, acertou=True).count()
        erros_categoria = desafio.flashcards.filter(flashcard__categoria=categoria, acertou=False).count()
        dados_categorias.append({
            'categoria': categoria,
            'acertos': acertos_categoria,
            'erros': erros_categoria,
        })

    # Ordenar categorias pelo percentual de acertos
    dados_categorias.sort(key=lambda x: x['acertos'] / (x['acertos'] + x['erros']) if (x['acertos'] + x['erros']) > 0 else 0, reverse=True)

    # Identificar as melhores e piores categorias
    melhores_categorias = [categoria for categoria in dados_categorias if (categoria['acertos'] / (categoria['acertos'] + categoria['erros']) * 100) > 70]
    piores_categorias = [categoria for categoria in dados_categorias if (categoria['acertos'] / (categoria['acertos'] + categoria['erros']) * 100) <= 70]

    # Ordenar melhores e piores categorias pelo percentual de acertos
    melhores_categorias.sort(key=lambda x: x['acertos'] / (x['acertos'] + x['erros']) * 100, reverse=True)
    piores_categorias.sort(key=lambda x: x['acertos'] / (x['acertos'] + x['erros']) * 100)
    


    return render(
        request,
        'flashcard/relatorio.html',
        {
            'desafio': desafio,
            'dados': dados,
            'categorias': name_categoria,
            'dados2': dados2,
            'melhores_categorias': melhores_categorias,
            'piores_categorias': piores_categorias,
        },
    )
