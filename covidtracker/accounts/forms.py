from django import forms
from .models import Patient, Doctor


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(EmployeeForm, self).__init__(*args, **kwargs)
    #     self.fields['position'].empty_label = "Select"
    #     self.fi3elds['emp_code'].required = False
