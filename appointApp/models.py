from django.db import models
from django.contrib.auth.models import User, AbstractUser,Permission, UserManager, Group

class Doctor(AbstractUser):
    degree = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    address = models.TextField()
    experience = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    number = models.CharField(max_length=15, blank=True, null=True)
    dateOfBirth = models.DateField(default=None)
    bio = models.TextField()
    registrationNumber = models.CharField(max_length=20, null=True, unique=True)
    registrationYear = models.PositiveIntegerField(default=0)
    workingHour = models.TextField(default="")
    specialization = models.TextField(default="")


    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='doctor_set',  # Change this to a unique related name
        related_query_name='doctor',
    )

    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='doctor_set',  # Change this to a unique related name
        related_query_name='doctor',
    )

    def __str__(self):
        return self.username


class Patient(AbstractUser):
    # Additional fields for the Patient profile
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10)
    address = models.TextField()
    description = models.TextField()

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='patient_set',  # Change this to a unique related name
        related_query_name='patient',
    )

    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='patient_set',  # Change this to a unique related name
        related_query_name='patient',
    )

    def __str__(self):
        return self.username

class Appointment(models.Model):
    appointmentId = models.AutoField(primary_key=True)  # Auto-incremented primary key
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')
    dateOfAppointment = models.DateField()
    timeOfAppointment = models.TimeField()

    def __str__(self):
        return f"Appointment ID: {self.AppointmentId}, Doctor: {self.Doctor.username}, Patient: {self.Patient.username}, Date: {self.DateOfAppointment}, Time: {self.TimeOfAppointment}"

class Treatment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_treatments')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_treatments')
    appointment_date = models.DateField()
    treatment_description = models.TextField()

    def __str__(self):
        return f"Treatment ID: {self.id}, Doctor: {self.doctor.username}, Patient: {self.patient.username}, Appointment Date: {self.appointment_date}"