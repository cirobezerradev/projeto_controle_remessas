from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cadastrar_remessa/', views.cadastrar_remessa, name='cadastrar_remessa'),
    path('cadastrar_remessa/xml/', views.abrir_xml, name='abrir_xml'),
    path('cadastrar_retorno/', views.cadastrar_retorno, name='cadastrar_retorno')
]
