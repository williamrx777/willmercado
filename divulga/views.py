from django.shortcuts import render,redirect
from .models import Produto

# Create your views here.

def novo_produto(request):
    if request.method == "GET":
        return render(request,'novo_produto.html')
    elif request.method == "POST":
        foto = request.FILES.get('foto')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        pais = request.POST.get('pais')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        

        produto = Produto(
            usuario=request.user,
            foto=foto,
            nome=nome,
            descricao=descricao,
            pais=pais,
            estado=estado,
            cidade=cidade,
        )

        produto.save()
        return render(request,'novo_produto.html')

def seus_produtos(request):
    if request.method =="GET":
        produto = Produto.objects.filter(usuario=request.user)
        return render(request,'seus_produtos.html', {'produto':produto})   

def remove_produto(request, id):
    produto = Produto.objects.get(id=id)

    if not produto.usuario == request.user:
        return redirect('/divulga/seus_produtos')

    produto.delete()
    return redirect('/divulga/seus_produtos')    
