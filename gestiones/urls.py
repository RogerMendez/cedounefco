from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='gestion-index'),
    path('new/', views.new_gestion, name='gestion-new'),
    path('<int:gestion_id>/select/', views.select_gestion, name='gestion-select'),
]