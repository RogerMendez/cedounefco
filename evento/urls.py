from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='evento-index'),
    path('new', views.new, name='evento-new'),
    path('<int:evento_id>/detail', views.detail_evento, name='evento-detail'),
]