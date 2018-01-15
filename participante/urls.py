from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='participante-index'),
    path('new', views.new, name='participante-new'),
    path('import', views.import_participante, name='participante-import'),

    path('<int:part_id>/update/', views.update_participante, name='participante-update'),
]