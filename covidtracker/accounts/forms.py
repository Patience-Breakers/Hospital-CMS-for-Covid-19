from django import forms
from .models import Patient, Doctor
from bootstrap_datepicker_plus import DatePickerInput


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'
