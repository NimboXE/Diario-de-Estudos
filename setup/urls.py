"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

## Importando os caminhos para a mídia ##
from django.conf.urls.static import static
from django.conf import settings

## Importando as views para a adição nos URLs ##
from app.views import *

## No fim do colchete, será implementado o caminho para os arquivos de mídia ##
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', paginaDeLogin, name='paginaDeLogin'),
    path('paginaDeCadastro/', paginaDeCadastro, name='paginaDeCadastro'),
    path('paginaHomeDoUsuario/', paginaHomeDoUsuario, name='paginaHomeDoUsuario'),
    path('logoutOption/', logoutOption, name='logoutOption'),
    path('paginaDeMaterias/', paginaDeMaterias, name='paginaDeMaterias'),
    path('paginaDeAnotacoes/', paginaDeAnotacoes, name='paginaDeAnotacoes'),
    path('paginaDeAtividades/', paginaDeAtividades, name='paginaDeAtividades'),
    path('paginaDoUsuario/', paginaDoUsuario, name='paginaDoUsuario'),
    path('paginaDeCadastroDeMateria/', paginaDeCadastroDeMateria, name='paginaDeCadastroDeMateria'), 
    path('paginaDeCadastroDeAnotacoes/', paginaDeCadastroDeAnotacoes, name='paginaDeCadastroDeAnotacoes'),
    path('deletarMateria/<id>', deletarMateria, name='deletarMateria'), 
    path('deletarAnotacao/<id>', deletarAnotacao, name='deletarAnotacao'), 
    path('paginaDeEdicaoDeAnotacao/<id>', paginaDeEdicaoDeAnotacao, name='paginaDeEdicaoDeAnotacao'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
