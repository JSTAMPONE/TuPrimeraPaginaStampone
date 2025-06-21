from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.EditarPerfilView.as_view(), name='editar_perfil'),
    path('mensaje/enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('mensajes/', views.bandeja_entrada, name='bandeja_entrada'),
    path('mensajes/enviados/', views.mensajes_enviados, name='mensajes_enviados'),
    path('mensajes/conversacion/<str:username>/', views.ver_conversacion, name='ver_conversacion'),
]