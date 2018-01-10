from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, Http404, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, AdminPasswordChangeForm
from django.conf import settings

from cedounefco.general_utility import admin_log_addition, admin_log_change
from gestiones.models import Gestion
from gestiones.form import GestionForm

@login_required(login_url='/login')
def index(request):
    gestiones = Gestion.objects.all()
    return render(request, 'gestiones/index.html', {
        'gestiones':gestiones,
    })

@login_required(login_url='/login')
def select_gestion(request, gestion_id):
    gestion = get_object_or_404(Gestion, pk = gestion_id)
    request.session['gestion'] = gestion.gestion
    sms = 'Gestion Seleccionada Correctamente'
    messages.success(request, sms)
    return HttpResponseRedirect(reverse(index))

@permission_required('gestiones.add_gestion', login_url='/login')
def new_gestion(request):
    if request.method == 'POST':
        form = GestionForm(request.POST)
        if form.is_valid():
            g = form.save()
            admin_log_addition(request, g, 'Gestion Registrada Correctamente')
            sms = 'Gestion Registrada Correctamente'
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index))
    else:
        form = GestionForm()
    return render(request, 'gestiones/new.html', {
        'form':form,
    })