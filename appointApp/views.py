from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "appointApp/index.html", {
        "patient_count":26787,
        "doctor_count":25,
        "stuff_count":1008298
    })


def register_doctor(request):
    if request == "POST":
        pass
    else:
        return render(request, "appointApp/register-doctor.html")

def register_patient(request):
    if request == "POST":
        pass
    else:
        return render(request, "appointApp/register-patient.html")