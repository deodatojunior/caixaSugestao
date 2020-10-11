from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

class SugestaoForm(ModelForm):
    class Meta:
        model = Sugestao
        fields = ('nome', 'texto', 'area_Da_Empresa')





def index(request):
    return render(request, 'appCaixaSugestao/index.html')

def sugestao_novo(request):
    form = SugestaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('obrigado')
    return render(request, 'appCaixaSugestao/sugestao_form.html', {'form': form})

def obrigado(request):
    return render(request, 'appCaixaSugestao/obrigado.html')

@login_required
def sugestao_listar(request):
    query = request.GET.get("busca")
    if query:
        sugestao = Sugestao.objects.filter(texto__iexact=query)
    else:
        sugestao = Sugestao.objects.all()
    sugestoes = {'lista': sugestao}
    return render(request, 'appCaixaSugestao/sugestao_listar.html', sugestoes)
@login_required
def sugestao_ver(request, pk):
    sugestao = get_object_or_404(Sugestao, pk=pk)
    return render(request, 'appCaixaSugestao/sugestao_ver.html', {'sugestao': sugestao})

@login_required
def sugestao_remover(request, pk):
    sugestao = Sugestao.objects.get(pk=pk)
    if request.method == "POST":
        sugestao.delete()
        return redirect('sugestao_listar')
    return render(request, 'appCaixaSugestao/sugestao_remover.html', {'sugestao': sugestao})

def logar(request):
    next = request.GET.get('next', '/usuario_listar/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, 'appCaixaSugestao/login.html', {'redirect_to': next})

@login_required
def deslogar(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def usuario_listar(request):
    usuarios = User.objects.all()
    usuario = {'lista': usuarios}
    return render(request, 'appCaixaSugestao/usuario_listar.html', usuario)

@login_required
def usuario_registrar(request):
    user = request.user
    if user.is_staff:
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            tipo = request.POST['tipo_usuario']
            if tipo == "administrador":
                user = User.objects.create_user(username, email, password)
                user.is_staff = True
                user.save()
            else:
                user = User.objects.create_user(username, email, password)

            return redirect('/usuario_listar/')
    else:
        messages.error(request, 'Permissão negada.')
        return redirect('/usuario_listar/')

    return render(request, 'appCaixaSugestao/usuario_registrar.html')


@login_required
def usuario_remover(request, pk):
    user = request.user
    if user.has_perm('user.delete_user'):
        try:
            usuario = User.objects.get(pk = pk)
            if request.method == "POST":
                usuario.delete()
                return redirect('usuario_listar')
        except:
            messages.error(request, 'Usuário não encontrado.')
            return redirect('/usuario_listar/')
    else:
        messages.error(request, 'Permissão negada.')
        return redirect('/usuario_listar/')

    return render(request, 'appCaixaSugestao/usuario_remover.html', {'usuario': usuario})
