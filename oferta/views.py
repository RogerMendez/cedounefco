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
from oferta.models import Ciclo, Curso
from gestiones.models import Gestion

from oferta.form import CicloForm, CursoForm, SearchCiclo

import xlrd
import os

@login_required(login_url='/login/')
def index(request):
    ciclo = ''
    gestion = Gestion.objects.get(gestion=request.session['gestion'])
    form = SearchCiclo(request.GET or None)
    if form.is_valid():
        ciclo = form.cleaned_data['ciclo']
    ciclos = Ciclo.objects.filter(gestion=gestion, ciclo__icontains=ciclo)
    return render(request, 'ciclos/index.html', {
        'ciclos':ciclos,
        'form':form,
    })

@permission_required('oferta.add_ciclo', login_url='/login/')
def new_ciclo(request):
    gestion = Gestion.objects.get(gestion=request.session['gestion'])
    if request.method == 'POST':
        form = CicloForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.gestion = gestion
            c.save()
            admin_log_addition(request, c, 'Ciclo Creado')
            sms = 'Ciclo Creado Correctamente'
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index))
    else:
        form = CicloForm()
    return render(request, 'ciclos/new.html', {
        'form':form,
    })

@permission_required('oferta.add_ciclo', login_url='/login/')
def import_ciclos(request):
    gestion = Gestion.objects.get(gestion=request.session['gestion'])
    location_file = os.path.join(settings.BASE_DIR, 'static')
    location_file = os.path.join(location_file, 'others')
    location_file = os.path.join(location_file, str('ciclos.xlsx'))
    workbook = xlrd.open_workbook(location_file)
    sheet = workbook.sheet_by_index(0)
    columnas = sheet.ncols
    filas = sheet.nrows
    for f in range(1, filas):
        c = sheet.cell_value(f, columnas - 1)
        ciclo = Ciclo.objects.get_or_create(
            ciclo = c,
            gestion = gestion
        )
        #ciclo.save()
        #admin_log_addition(request, ciclo, 'Ciclo Registrado')
    total = filas - 1
    sms = 'Se Importaron %s Ciclos'%total
    messages.success(request, sms)
    return HttpResponseRedirect(reverse(new_ciclo))

@permission_required('oferta.add_curso', login_url='/login/')
def new_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save()
            admin_log_addition(request, curso, 'Curso Registrado')
            sms = 'Curso Registrado Correctamente'
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index))
    else:
        form = CursoForm()
    return render(request, 'cursos/new.html', {
        'form':form,
    })

@permission_required('oferta.add_curso', login_url='/login/')
def import_curso(request):
    gestion = Gestion.objects.get(gestion=request.session['gestion'])
    location_file = os.path.join(settings.BASE_DIR, 'static')
    location_file = os.path.join(location_file, 'others')
    location_file = os.path.join(location_file, str('cursos.xlsx'))
    workbook = xlrd.open_workbook(location_file)
    sheet = workbook.sheet_by_index(0)
    columnas = sheet.ncols
    filas = sheet.nrows
    #c = sheet.cell_value(0, 1)#(fila, columna)
    for f in range(1, filas):
        ci = sheet.cell_value(f, 0)
        cu = sheet.cell_value(f, 1)
        if Ciclo.objects.filter(gestion=gestion, ciclo__icontains=ci):
            ciclo = Ciclo.objects.filter(gestion=gestion, ciclo__icontains=ci).first()
            curso = Curso.objects.get_or_create(
                curso = cu,
                ciclo = ciclo,
            )
            #curso.save()
            #admin_log_addition(request, curso, 'Curso Registrado')
        else:
            print(ci)

    total = filas - 1
    sms = 'Se Importaron Correctamente los Cursos'
    messages.success(request, sms)
    return HttpResponseRedirect(reverse(new_curso))

@login_required(login_url='/login/')
def cursos_ciclo(request, ciclo_id):
    ciclo = get_object_or_404(Ciclo, pk = ciclo_id)
    cursos = Curso.objects.filter(ciclo=ciclo)
    return render(request, 'ciclos/cursos_ciclo.html', {
        'cursos':cursos,
        'ciclo':ciclo,
    })

@permission_required('oferta.delete_ciclo')
def delete_ciclo(request, ciclo_id):
    ciclo = get_object_or_404(Ciclo, pk = ciclo_id)
    try:
        ciclo.delete()
        messages.error(request, 'Ciclo Eliminado')
    except ProtectedError as ex:
        messages.error(request, 'No se Puede Eliminar el Ciclo')
        messages.error(request, 'Elimine los Cursos del Ciclo ')
    return HttpResponseRedirect(reverse(index))