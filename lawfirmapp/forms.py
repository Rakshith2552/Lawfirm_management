from django import forms
from lawfirmapp.models import AdvocateProfile,Enquriy,Appointment

class AdvocateForm(forms.ModelForm):
    class Meta:
        model=AdvocateProfile
        fields= '__all__'

class EnquiryForm(forms.ModelForm):
    class Meta:
        model=Enquriy
        fields= '__all__'
        # fields=['name','phone','email','address','case_type','description','any_doc']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields= '__all__'
        