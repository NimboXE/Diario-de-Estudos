from django.shortcuts import render, redirect

## Importando as funções para login, authenticate e logout ##
from django.contrib.auth import login, logout, authenticate

## Importando o decorador para a obrigação do login ##
from django.contrib.auth.decorators import login_required

## Importando os modelos do banco de dados ##
from app.models import Usuario, Materia, Atividade, PlanoDeEstudos, Anotacao

# Create your views here.

## Pagina para o login onde da acesso à home do usuário ##
def paginaDeLogin(request):

    ## Verificação para o método da requisição ##
    if request.method == "POST":

        ## Coletando os dados inseridos pelo usuário ##
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        ## Autenticando o usuário ##
        usuario = authenticate(username=email, password=senha)
        print(usuario)

        ## Verificando a existencia do usuário ##
        if usuario is not None:

            ## Logando o usuário ##
            login(request, usuario)

            ## Redirecionando o usuário para a página home do próprio ##
            return redirect(paginaHomeDoUsuario)

    return render(request, 'paginaDeLogin.html')

## Pagina para o cadastro de novos usuários ##
def paginaDeCadastro(request):

    ## Verificação para o método da requisição ##
    if request.method == "POST":

        ## Coletando os dados inseridos pelo usuário ##
        nomeDeUsuario = request.POST.get("nomeDeUsuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        ## Criando o novo usuário ##
        Usuario.objects.create_user(nome=nomeDeUsuario, username=email, email=email, password=senha)

        ## Redirecionando o novo usuário para a página de login ##
        return redirect(paginaDeLogin)

    return render(request, 'paginaDeCadastro.html')

## Pagina home do usuário (Apartir daqui, as paginas precisarão ter feito o login. Essa verificação será feita com o decorador) ##
@login_required(login_url=paginaDeLogin)
def paginaHomeDoUsuario(request):

    ## Pegando as atividades do usuário para o envio ##
    atividades = Atividade.objects.filter(usuario_fk=request.user)

    return render(request, 'paginaHomeDoUsuario.html', {'atividades':atividades})

## Função para o logout do usuário ##
@login_required(login_url=paginaDeLogin)
def logoutOption(request):

    logout(request)

    return redirect(paginaDeLogin)

## Pagina de matérias do usuário ##
@login_required(login_url=paginaDeLogin)
def paginaDeMaterias(request):

    materias = Materia.objects.filter(usuario=request.user)

    return render(request, 'paginaDeMateria.html', {'materias':materias})

## Pagina de anotações do usuário ##
@login_required(login_url=paginaDeLogin)
def paginaDeAnotacoes(request):

    anotacoes = Anotacao.objects.filter(usuario_fk=request.user)

    return render(request, 'paginaDeAnotacoes.html', {'anotacoes':anotacoes})

## Pagina de atividades do usuário ##
@login_required(login_url=paginaDeLogin)
def paginaDeAtividades(request):
    return render(request, 'paginaDeAtividades.html')

## Pagina de usuário ##
@login_required(login_url=paginaDeLogin)
def paginaDoUsuario(request):

    quantidadeDeMaterias = Materia.objects.filter(usuario = request.user).count()
    quantidadeDeAnotacoes = Anotacao.objects.filter(usuario_fk = request.user).count()
    quantidadeDeAtividadesConcluidas = Atividade.objects.filter(usuario_fk = request.user, situacao = "Concluída").count()

    if request.method == "POST":
        
        nome = request.POST.get("nome")
        informacoes = request.POST.get("informacoes")

        usuario = request.user

        usuario.nome = nome
        usuario.informacoes = informacoes

        usuario.save()

    return render(request, 'paginaDoUsuario.html', {'quantidadeDeMaterias':quantidadeDeMaterias, 'quantidadeDeAnotacoes':quantidadeDeAnotacoes, 'quantidadeDeAtividadesConcluidas':quantidadeDeAtividadesConcluidas})

## Pagina de cadastro de matérias ##
@login_required(login_url=paginaDeLogin)
def paginaDeCadastroDeMateria(request):

    if request.method == "POST":

        nome = request.POST.get("nome")

        Materia.objects.create(nome=nome, usuario=request.user)

        return redirect(paginaDeMaterias)

    return render(request, 'paginaDeCadastroDeMateria.html')

## Pagina de cadastro de anotações ##
@login_required(login_url=paginaDeLogin)
def paginaDeCadastroDeAnotacoes(request):

    if request.method == "POST":

        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")

        Anotacao.objects.create(titulo=titulo, descricao=descricao, usuario_fk=request.user)

        return redirect(paginaDeAnotacoes)

    return render(request, 'paginaDeCadastroDeAnotacao.html')

## Função para deletar uma matéria ##
@login_required(login_url=paginaDeLogin)
def deletarMateria(request, id):

    materia = Materia.objects.get(id=id)
    materia.delete()

    return redirect(paginaDeMaterias)

## Função para deletar uma anotação ##
@login_required(login_url=paginaDeLogin)
def deletarAnotacao(request, id):

    anotacao = Anotacao.objects.get(id=id)
    anotacao.delete()

    return redirect(paginaDeAnotacoes)

## Função para deletar uma anotação ##
@login_required(login_url=paginaDeLogin)
def paginaDeEdicaoDeAnotacao(request, id):

    anotacao = Anotacao.objects.get(id=id)

    if request.method == "POST":

        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")

        anotacao.titulo = titulo
        anotacao.descricao = descricao

        anotacao.save()

        return redirect(paginaDeAnotacoes)

    return render(request, 'paginaDeEdicaoDeAnotacao.html', {'anotacao':anotacao})