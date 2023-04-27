from http.client import ImproperConnectionState
import imp
from operator import index
from django.urls import path
from planning.views import indexApp
from . import views

urlpatterns = [
    path('', indexApp, name="indexApp"),
    path('dashboard/entrainement/', views.create_entrainement, name='create_entrainement'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/entrainement/<str:titre>/', views.modifEntrainement, name='modifEntrainement'),
    path('dashboard/entrainement/delete/<str:titre>/', views.deleteEntrainement, name='deleteEntrainement'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
]