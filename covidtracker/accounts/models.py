from django.db import models

# Create your models here.


class Patient (models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=1000)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)  # M of F
    phone = models.TextField(max_length=1000)
    address = models.TextField(max_length=1000)
    email_id = models.EmailField(max_length=254)
    date = models.DateField(auto_now=False, auto_now_add=False)
    # Hospital
    room_no = models.IntegerField(default=0)
    floor_no = models.IntegerField(default=0)
    o2_level = models.IntegerField(default=0)
    temperature = models.IntegerField(default=97)

    doctorId = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Room (models.Model):
    floor_no = models.IntegerField(default=0)
    room_no = models.IntegerField(default=0)
    ventilator = models.BooleanField(default=False)
    occupied = models.BooleanField(default=False)
    patient_id = models.IntegerField(default=0)

    def __int__(self):
        return self.floor_no


class Doctor (models.Model):

    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, default="")
    phone = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    # in years
    no_of_patients = models.IntegerField(default=0)
    no_of_recovered_patients = models.IntegerField(default=0)
    no_of_decreased_patients = models.IntegerField(default=0)
    no_of_patients_on_ventilator = models.IntegerField(default=0)

    def __str__(self):
        return self.doctor_id


class Result (models.Model):
    patient_id = models.IntegerField(default=0)
    patient_name = models.CharField(default="", max_length=500)
    asymptomatic = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)
    fever = models.BooleanField(default=False)
    apetite_loss = models.BooleanField(default=False)
    # todo Here 3 denotes the no of test before (1 being the latest and 3 being the oldest)
    covid_test_result_3 = models.BooleanField(default=True)
    covid_test_result_2 = models.BooleanField(default=True)
    covid_test_result_1 = models.BooleanField(default=True)

    def __str__(self):
        return self.patient_name+" "+patient_id
