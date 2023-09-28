from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('register-doctor', views.register_doctor, name="register_doctor"),
    path('register-patient', views.register_patient, name="register_patient"),
<<<<<<< HEAD
    path('contact-us', views.contact_us, name="contact_us"),
    path('about-us', views.about_us, name="about_us"),
    path('appointment', views.appointment, name="appointment")
=======
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout")
>>>>>>> main
]
