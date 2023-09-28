from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


from .models import Doctor, User

# Create your views here.
def index(request):
    return render(request, "appointApp/index.html", {
        "patient_count":26787,
        "doctor_count":25,
        "stuff_count":1008298
    })


def register_doctor(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        number = request.POST["number"]
        password = request.POST["password"]
        confirmPassword = request.POST["confirm-password"]
        pincode = request.POST["pincode"]
        dateOfBirth = request.POST["date-of-birth"]
        gender = request.POST["gender"]
        registrationNumber = request.POST["registration-number"]
        registrationYear = request.POST["registration-year"]
        workingHour = request.POST["working-hours"]
        degree = request.POST["degree"]
        specialization = request.POST["specialization"]

        print(name,email,number,password, confirmPassword, pincode, dateOfBirth, gender, registrationNumber, registrationYear, workingHour, degree, specialization)

        if password != confirmPassword:
            return render(request, "appointApp/register-doctor.html", {
                "message": "Passwords must match"
            })
        try:
            doctor = Doctor.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name = name,
                number = number,
                pincode = pincode,
                dateOfBirth = dateOfBirth,
                gender = gender,
                registrationNumber = registrationNumber,
                registrationYear = registrationYear,
                workingHour = workingHour,
                degree = degree,
                specialization = specialization
            )
            doctor.save()
        except IntegrityError:
            return render(request, "appointApp/register-doctor.html", {
                "message": "Username already taken."
            })
        login(request, doctor)
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "appointApp/register-doctor.html")

def register_patient(request):
    print("HERE")
    if request == "POST":
        pass
    else:
        return render(request, "appointApp/register-patient.html")

def contact_us(request):
    if request == "POST":
        pass
    else:
        return render(request, "appointApp/contact-us.html")

def about_us(request):
    if request == "POST":
        pass
    else:
        return render(request, "appointApp/about-us.html")

def appointment(request):
    if request == "POST":
        pass
    else:
        return render(request, "appointApp/appointment.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        if not email or not password:
            return render(request, "appointApp/login.html", {
                "message": "Email or Password field are empty!"
            })
        doctor = authenticate(request=request, username=email, password=password)

        if doctor is not None:
            login(request, doctor)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "appointApp/login.html", {
                "message":"Invalid Username or Password"
            })
    else:
        return render(request, "appointApp/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
