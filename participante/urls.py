from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='participante-index'),
    path('new', views.new, name='participante-new'),
    path('import', views.import_participante, name='participante-import'),

    #path('<int:ciclo_id>/cursos/', views.cursos_ciclo, name='ciclo-cursos'),
]