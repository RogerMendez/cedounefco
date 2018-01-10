from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ciclos-index'),
    path('new', views.new_ciclo, name='ciclos-new'),
    path('import', views.import_ciclos, name='ciclos-import'),
    path('curso/new', views.new_curso, name='cursos-new'),
    path('curso/import', views.import_curso, name='cursos-import'),
    path('<int:ciclo_id>/cursos/', views.cursos_ciclo, name='ciclo-cursos'),
    path('<int:ciclo_id>/delete/', views.delete_ciclo, name='ciclo-delete'),
]