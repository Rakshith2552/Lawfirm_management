from django.shortcuts import render,redirect
from lawfirmapp.forms import AdvocateForm,EnquiryForm,AppointmentForm
from lawfirmapp.models import AdvocateProfile,AllCases,Enquriy,Appointment
from lawfirmapp.utils import send_email_view


# Create your views here.
def home(request):
    casedata=AllCases.objects.all()
    return render(request,'lawfirm/home.html',{'casedata':casedata})

def allCases(request):
    casedata=AllCases.objects.all()
    return render(request,'lawfirm/allcases.html',{'casedata':casedata})

def about(request):
    data=AdvocateProfile.objects.last()
    return render(request,'lawfirm/about.html',{'firm':data})

def lawprofile(request):
    form=AdvocateForm()
    if request.method=='POST':
        form=AdvocateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("Submitted")
            return redirect('about')
    return render(request,'lawfirm/profile.html',{'form':form})

def enquiry(request):
    form=EnquiryForm()
    if request.method == 'POST':
        form=EnquiryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("Submitted")
            return redirect('enquiry')
    return render(request,'lawfirm/enquiry.html',{'form':form})

def appointment(request):
    form=AppointmentForm()
    if request.method=='POST':
        form=AppointmentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("Submitted")
            email=form.cleaned_data['email']
            print(email)
            email=form.cleaned_data['email']
            response=send_email_view(email)
            return redirect('appointment')
    appointments=Appointment.objects.all()
    return render(request,'lawfirm/appointment.html',{'appointment':form,'appointments':appointments})

def contact(request):
    return render(request,'lawfirm/contact.html',{})
