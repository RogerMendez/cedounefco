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

from cedounefco.paginator import Paginate
from cedounefco.general_utility import admin_log_addition, admin_log_change
from participante.models import Participante
from participante.form import ParticipanteForm, ParticipanteSearch
import xlrd
import os

@login_required(login_url='/login/')
def index(request):
    ci = ''
    materno = ''
    paterno = ''
    form = ParticipanteSearch(request.GET or None)
    if form.is_valid():
        ci = form.cleaned_data['ci']
        paterno = form.cleaned_data['paterno']
        materno = form.cleaned_data['materno']
    participantes = Participante.objects.filter(ci__icontains=ci, paterno__icontains=paterno, materno__icontains=materno)
    pag = Paginate(request, participantes, 50)
    return render(request, 'participantes/index.html', {
        'participantes':pag['queryset'],
        'posts': pag['queryset'],
        'totPost': participantes,
        'paginator': pag,
        'form':form,
    })

@permission_required('participantes.add_participantes', login_url='/login/')
def new(request):
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            p = form.save()
            admin_log_addition(request, p, 'Participante Registrado')
            sms = 'Participantes Registrado Correctamente'
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index))
    else:
        form = ParticipanteForm()
    return render(request, 'participantes/new.html', {
        'form':form,
    })

@permission_required('participantes.add_participantes', login_url='/login/')
def import_participante(request):
    location_file = os.path.join(settings.BASE_DIR, 'static')
    location_file = os.path.join(location_file, 'others')
    location_file = os.path.join(location_file, str('participantes.xlsx'))
    workbook = xlrd.open_workbook(location_file)
    sheet = workbook.sheet_by_index(0)
    columnas = sheet.ncols
    filas = sheet.nrows
    for f in range(0, filas):
        ci = int(sheet.cell_value(f, 0))
        rda = int(sheet.cell_value(f, 1))
        paterno = sheet.cell_value(f, 2)
        materno = sheet.cell_value(f, 3)
        nombre1 = sheet.cell_value(f, 4)
        nombre2 = sheet.cell_value(f, 5)
        sexo = int(sheet.cell_value(f, 6))
        p = Participante.objects.get_or_create(
            ci=ci,
            rda=rda,
            nombre1=nombre1,
            nombre2=nombre2,
            paterno=paterno,
            materno=materno,
            sexo=sexo,
        )
        # ciclo.save()
        # admin_log_addition(request, ciclo, 'Ciclo Registrado')
    total = filas - 1
    sms = 'Se Importaron %s Participantes' % total
    messages.success(request, sms)
    return HttpResponseRedirect(reverse(new))

@permission_required('participantes.change_participantes', login_url='/login/')
def update_participante(request, part_id):
    participante = get_object_or_404(Participante, pk = part_id)
    if request.method == 'POST':
        form = ParticipanteForm(request.POST, instance=participante)
        if form.is_valid():
            p = form.save()
            admin_log_change(request, p, 'Participante Modificado')
            sms = 'Participantes Modificado Correctamente'
            messages.warning(request, sms)
            return HttpResponseRedirect(reverse(index))
    else:
        form = ParticipanteForm(instance=participante)
    return render(request, 'participantes/update.html', {
        'form':form,
    })