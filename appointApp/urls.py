from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register-doctor', views.register_doctor, name="register_doctor"),
    path('register-patient', views.register_patient, name="register_patient"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout")
]
