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


#def local(request, titulo_evento):
    #Evento.objects.get(titulo= titulo_evento)
    #return HttpResponse(f'Local:{Evento.Local}');

