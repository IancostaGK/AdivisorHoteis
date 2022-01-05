from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('meus_posts', views.meus_posts, name="meus_posts"),
    path('cria/post', views.cria_post, name='cria_post'),
    path('deleta/<int:postagem_id>',views.deleta_post, name='deleta_post'),
]