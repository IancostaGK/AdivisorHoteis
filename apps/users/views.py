from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from postagens.models import Postagem2
# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Email e senha são obrigatorios')
            return redirect('login')
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('meus_posts')
            
        else:
            messages.error(request, 'Email ou Senha não conferem')
            
            
    return render(request, 'users/login.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['username']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        
        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request,'Usuário já cadastrado')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        
        return redirect('login')
    else:
        return render(request,'users/cadastro.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def campo_vazio(campo):
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2