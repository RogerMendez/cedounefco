from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, Http404, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, AdminPasswordChangeForm
from django.conf import settings
from django.utils.encoding import smart_str

from gestiones.models import Gestion
from users.form import UsernameForm

def home(request):

    return render(request, 'base.html')

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse(user_index))
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            access = authenticate(username=username, password=password)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    g = Gestion.objects.all().values('gestion')
                    a = g.latest('gestion')
                    request.session['gestion'] = a['gestion']
                    if 'next' in request.GET:
                        msm = "Inicio de Sesion Correcto <strong> Gracias Por Su Visita</strong>"
                        messages.add_message(request, messages.INFO, msm)
                        return HttpResponseRedirect(str(request.GET['next']))
                    else:
                        msm = "Inicio de Sesion Existoso  <strong>Gracias Por Su Visita</strong>"
                        messages.add_message(request, messages.SUCCESS, msm)
                        return HttpResponseRedirect(reverse(user_index))
                else:
                    sms = "Su Cuenta No Esta Activada <strong>Contactese con el Administrador</strong>"
                    messages.warning(request, sms)
                    return HttpResponseRedirect(reverse(user_index))
            else:
                sms = "Usted No Es Usuario Del Sistema"
                #messages.add_message(request, messages.ERROR, msm, 'danger')
                messages.error(request, sms)
                return HttpResponseRedirect(reverse(user_login))
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {
        'form': form,
    })

@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    sms = 'Gracias Por Su Visita'
    messages.info(request, sms)
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def user_index(request):

    return render(request, 'users/index.html', {
    })

@login_required(login_url='/login/')
def reset_pass(request):
    if request.method == 'POST' :
        form = AdminPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(user_index))
    else:
        form = AdminPasswordChangeForm(user=request.user)
    return  render(request,'users/reset_pass.html', {
        'form' :form,
        })

@login_required(login_url='/login/')
def change_username(request):
    if request.method == 'POST' :
        form = UsernameForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            sms = 'Nombre De Usuario Modificado Correctamente'
            messages.info(request, sms)
            return HttpResponseRedirect(reverse(user_index))
    else:
        form= UsernameForm(instance=request.user)
    return  render(request, 'users/change_username.html', {
        'form' :form,
    })
