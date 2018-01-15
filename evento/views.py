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
from django.db.models import ProtectedError

from cedounefco.general_utility import admin_log_addition, admin_log_change

from evento.models import Evento, Detalle, PartEvento
from gestiones.models import Gestion

from evento.form import EventoForm

@login_required(login_url='/login/')
def index(request):
    gestion = Gestion.objects.get(gestion=request.session['gestion'])
    eventos = Evento.objects.filter(gestion = gestion)
    return render(request, 'eventos/index.html', {
        'eventos':eventos,
    })

@login_required(login_url='/login')
def new(request):
    gestion = Gestion.objects.get(gestion=request.session['gestion'])
    if request.method == 'POST':
        form = EventoForm()
        if form.is_valid():
            evento = form.save(commit=False)
            evento.user = request.user
            evento.gestion = gestion
            evento.save()
            admin_log_addition(request, 'Evento Regsitrado')
            sms = 'Evento Registrado Correctamente'
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index))
    else:
        form = EventoForm()
    return render(request, 'eventos/new.html', {
        'form':form,
    })

@login_required(login_url='/login/')
def detail_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk = evento_id)

    return render(request, 'eventos/detail.html', {
        'evento':evento,
    })