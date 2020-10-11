from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sugestao_form/', views.sugestao_novo, name='sugestao_novo'),
    path('sugestao_listar/', views.sugestao_listar, name='sugestao_listar'),
    path('sugestao_ver/<int:pk>', views.sugestao_ver, name='sugestao_ver'),
    path('sugestao_remover/<int:pk>', views.sugestao_remover, name='sugestao_remover'),
    path('obrigado/', views.obrigado, name='obrigado'),


    path('login/', views.logar, name='login'),
    path('deslogar/', views.deslogar, name='deslogar'),


    path('usuario_registrar/', views.usuario_registrar, name='usuario_registrar'),
    path('usuario_listar/', views.usuario_listar, name='usuario_listar'),
    path('usuario_remover/<int:pk>', views.usuario_remover, name='usuario_remover')


]