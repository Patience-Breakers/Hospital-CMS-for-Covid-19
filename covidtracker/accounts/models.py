from django.db import models

# Create your models here.


class Patient(models.Model):

    name = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)  # M of F
    phone = models.TextField()
    address = models.TextField()
    emailId = models.EmailField(max_length=254)
    date = models.DateField(auto_now=False, auto_now_add=False)

    # Hospital

    bedNo = models.IntegerField(default=0)
    floor = models.IntegerField(default=0)
    o2level = models.IntegerField(default=0)
    asymptomatic = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)
    fever = models.BooleanField(default=False)
    apetiteLoss = models.BooleanField(default=False)
    temperature = models.IntegerField(default=97)
    recovered = models.BooleanField(default=False)
    admitted = models.BooleanField(default=True)
    onVentilator = models.BooleanField(default=False)
    decreased = models.BooleanField(default=False)
    status = models.CharField(max_length=20)
    # admitted , recovered , decreased, or on ventilator

    thirdastCOvidResult = models.BooleanField(default=True)
    secondlastCovidResult = models.BooleanField(default=True)
    lastCovidResult = models.BooleanField(
        default=True)  # true for covid positive

    # If(all three are false)

    daysAdmitted = models.IntegerField(default=0)
    doctorId = models.IntegerField(default=0)
