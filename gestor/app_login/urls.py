from django.urls import path
from . import views

#Nombre del espacio para las URLs de autenticación
app_name = 'auth'

urlpatterns = [
    #Autenticación - login, logout, register
    path('login/', views.LoginView, name='login'),
    path('register/', views.RegisterView, name='register'),
    path('logout/', views.LogoutView, name='logout'),
]