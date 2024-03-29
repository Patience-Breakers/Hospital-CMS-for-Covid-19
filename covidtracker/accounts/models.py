from django.db import models


class ItemsTotalCount(models.Model):
    vaccines = models.IntegerField(default=0)
    vaccines_used = models.IntegerField(default=0)
    ppe_kits = models.IntegerField(default=0)
    ppe_kits_used = models.IntegerField(default=0)
    ventilator = models.IntegerField(default=0)


class Doctor (models.Model):

    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, default="")
    phone = models.CharField(default="", max_length=500)
    experience_in_years = models.IntegerField(default=0)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Result (models.Model):
    Covid_test = models.CharField(default="", max_length=500)

    def __str__(self):
        return self.Covid_test


class Room (models.Model):
    floor_no = models.IntegerField(default=0)
    room_no = models.CharField(default="", max_length=500)
    ventilator = models.BooleanField(default=False)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.room_no


class Patient (models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    GENDERS = (
        (u'M', u'Male'),
        (u'F', u'Female'),
        (u'T', u'Transgender'),
        (u'O', u'Others'),

    )
    gender = models.CharField(max_length=2, null=True,
                              choices=GENDERS, default='M')
    phone = models.CharField(max_length=13)
    address = models.TextField(max_length=100)
    email_id = models.EmailField(max_length=254)
    date_admitted = models.DateField(auto_now=False, auto_now_add=False)
    oxygen_level = models.IntegerField(default=90)
    temperature = models.IntegerField(default=97)
    decreased = models.BooleanField(default=False)
    recovered = models.BooleanField(default=False)

    # todo foreign keys models
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default="")
    covid_test_result = models.ForeignKey(
        Result, on_delete=models.CASCADE, default="")
    room_no_and_bed_no = models.ForeignKey(
        Room, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.name
