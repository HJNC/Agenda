from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from core.models import Evento

#so entra na pagina se estiver logado
from django.contrib.auth.decorators import login_required

#fazer autenticaçao
from django.contrib.auth import authenticate, login, logout



#pagina de login se nao tiver logado, sera redirecionado
def login_user(request):
    return render(request,'login.html')

#vai autenticar o login
def submit_login(request):

    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')

        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuario ou senha invalido!")
    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


#vai verificar se esta logado
@login_required(login_url='/login/')

# Create your views here.
def lista_eventos(request):
    #evento = Evento.objects.get(id=1) - pegar apenas um item da lista
    usuario = request.user# - identifica qual usuario esta logado
    evento = Evento.objects.filter(usuario=usuario)# -- so mostra os evento do proprio usuario


    #evento = Evento.objects.all


    dados={'eventos':evento}

    return render(request, 'agenda.html', dados)


#criar pagina de cadastro de eventos - inclusao de dados


@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados= {}

    if id_evento:
        dados['evento']=Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        local_evento=request.POST.get('local_evento')
        usuario = request.user
        id_evento= request.POST.get('id_evento')

        if id_evento:
            Evento.objects.filter(id=id_evento).update(titulo=titulo, data_evento=data_evento, descricao=descricao,
                               local_evento=local_evento)

        else:
                #vai enviar os dados para o banco de dados

            Evento.objects.create(titulo=titulo, data_evento=data_evento, descricao=descricao,
                              usuario=usuario, local_evento=local_evento)


    return redirect('/')



#excluir arquivos
@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)

    if usuario == evento.usuario:
        evento.delete()

    return redirect('/')



