from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView as DjangoLogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Perfil, Mensaje
from django.utils.decorators import method_decorator
from django.views import View
from .forms import UserForm, PerfilForm, MensajeForm
from django.contrib import messages
from django.db.models import Q

class LoginView(LoginView):
    template_name = 'accounts/login.html'

class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('inicio')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        Perfil.objects.get_or_create(user=self.object)
        return response

@login_required
def perfil(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'accounts/perfil.html', {'perfil': perfil})
    
@method_decorator(login_required, name='dispatch')
class EditarPerfilView(View):
    def get(self, request):
        user_form = UserForm(instance=request.user)
        perfil_form, _ = Perfil.objects.get_or_create(user=request.user)
        perfil_form = PerfilForm(instance=request.user.perfil)
        return render(request, 'accounts/editar_perfil.html', {
            'user_form': user_form,
            'perfil_form': perfil_form
        })

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        perfil, _ = Perfil.objects.get_or_create(user=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfil')
        messages.error(request, 'Hubo un error al actualizar tu perfil.')
        return render(request, 'accounts/editar_perfil.html', {
            'user_form': user_form,
            'perfil_form': perfil_form
        })
    
@login_required
def enviar_mensaje(request):
    destinatario_username = request.GET.get('para')
    inicial = {}

    if destinatario_username:
        try:
            destinatario = User.objects.get(username=destinatario_username)
            inicial['destinatario'] = destinatario
        except User.DoesNotExist:
            pass

    if request.method == 'POST':
        form = MensajeForm(request.POST, user=request.user)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            messages.success(request, 'Mensaje enviado con éxito.')
            return redirect('bandeja_entrada')
        else:
            messages.error(request, 'No se pudo enviar el mensaje.')
    else:
        form = MensajeForm(initial=inicial, user=request.user)

    return render(request, 'accounts/enviar_mensaje.html', {'form': form})

@login_required
def bandeja_entrada(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    usuarios = User.objects.exclude(id=request.user.id).exclude(username='adminapptorneo')
    return render(request, 'accounts/bandeja_entrada.html', {'mensajes': mensajes, 'usuarios': usuarios})

@login_required
def mensajes_enviados(request):
    mensajes = Mensaje.objects.filter(remitente=request.user).order_by('-fecha_envio')
    return render(request, 'accounts/mensajes_enviados.html', {'mensajes': mensajes})

@login_required
def ver_conversacion(request, username):
    otro_usuario = User.objects.get(username=username)
    mensajes = Mensaje.objects.filter(
        Q(remitente=request.user, destinatario=otro_usuario) | 
        Q(remitente=otro_usuario, destinatario=request.user)
    ).order_by('fecha_envio')

    if request.method == 'POST':
        cuerpo = request.POST.get('cuerpo')
        if cuerpo:
            Mensaje.objects.create(
                remitente=request.user,
                destinatario=otro_usuario,
                asunto='Conversación',
                cuerpo=cuerpo
            )
            messages.success(request, 'Mensaje enviado')
            return redirect('ver_conversacion', username=otro_usuario.username)
        else:
            messages.error(request, 'El mensaje no puede estar vacío')

    return render(request, 'accounts/conversacion.html', {
        'mensajes': mensajes,
        'otro_usuario': otro_usuario,
    })