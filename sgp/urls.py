from django.contrib import admin
from django.urls import path
from sgpapp.views import index, gerenciar, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('gerenciar/', gerenciar, name='gerenciar'),
    path('signup/', signup, name='signup'),
]
