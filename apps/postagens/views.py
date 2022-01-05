from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from postagens.models import Postagem2

# Create your views here.
def home(request):
    
    postagem = Postagem2.objects.order_by('-date_post')
    
    dados = {
        'postagens' : postagem
    }
    
    return render(request,'postagens/home.html', dados)

def meus_posts(request):
    if request.user.is_authenticated:
        pessoa_id = request.user.id
        print(pessoa_id)
        post = Postagem2.objects.order_by('-date_post').filter(pessoa=pessoa_id)
        print(post)
        dados = { 
            'postagens' : post
        }
        return render(request, 'postagens/meus_posts.html', dados)
    else:
        return redirect('index')

def cria_post(request):
    if request.method == 'POST':
        now = datetime.now()
        titulo = request.POST['titulo']
        comentario = request.POST['comentario']
        nota = request.POST['nota']
        foto = request.FILES['foto']
        date_post = now.strftime("%Y-%m-%d %H:%M")
        user = get_object_or_404(User, pk=request.user.id)
        postagem = Postagem2.objects.create(pessoa=user,titulo=titulo, comentario=comentario, nota=nota, date_post=date_post, foto=foto)
        postagem.save()
        return redirect('meus_posts')
    else:
        return render(request, 'postagens/criar_postagem.html')

def deleta_post(request, postagem_id):
    print(postagem_id)
    post = get_object_or_404(Postagem2, pk=postagem_id )
    post.delete()
    return redirect('meus_posts')