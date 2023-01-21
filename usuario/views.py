from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            
            return render(request, 'cadastro.html')
        
        if senha != confirmar_senha:
            
            return render(request, 'cadastro.html')

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
           
            return render(request, 'cadastro.html')
        except:
            
            return render(request, 'cadastro.html')

def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome,
                      password=senha)

    if user is not None:
      login(request, user)
      return redirect('/divulga/novo_produto')
    if request.user.is_authenticated:
        return redirect('/divulga/novo_produto')
    else:
      
      return render(request, 'login.html')    

def sair(request):
    logout(request)
    return redirect('/usuario/cadastro')