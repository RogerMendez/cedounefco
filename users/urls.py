from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('users/index', views.user_index, name='users-index'),
    path('change/pass/', views.reset_pass, name='user-reset-pass'),
    path('change/username/', views.change_username, name='user-change-username'),
]