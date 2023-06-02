from django.contrib import admin
from django.urls import path
from sgpapp.views import index, gerenciar, cadastro, lista_servidores, editar_servidor, apagar_servidor, detalhar_servidor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('gerenciar/', gerenciar, name='gerenciar'),
    path('cadastro/', cadastro, name='cadastro'),
    path('lista_servidores/', lista_servidores, name='lista_servidores'),
    path('editar_servidor/<int:servidor_id>/', editar_servidor, name='editar_servidor'),
    path('apagar_servidor/<int:servidor_id>/', apagar_servidor, name='apagar_servidor'),
    path('servidor/<int:id>/', detalhar_servidor, name='detalhar_servidor'),


]
