
from django.contrib import admin

from .models import Patient, Doctor, Room, Result
# # Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Room)
admin.site.register(Result)
