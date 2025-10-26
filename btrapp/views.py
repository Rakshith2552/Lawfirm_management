from django.shortcuts import render,redirect
from btrapp.forms import UserForm,UserProfileForm,UserUpdateForm,UserProfileUpdateForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from btrapp.models import ModelName,CaseManagement
# Create your views here.

def register(request):
    registered=False
    if request.method=='POST':
        form=UserForm(request.POST)
        form1=UserProfileForm(request.POST,request.FILES)
        
        if form.is_valid() and form1.is_valid():
            # print(form.cleaned_data['username'])
            # print(form1.cleaned_data['city'])
            user=form.save()
            user.set_password(user.password)
            user.save()
            
            profile=form1.save(commit=False)
            profile.user=user #we are merging two models
            profile.save()
            registered=True
    else:
        form=UserForm()
        form1=UserProfileForm()
        
    context={
        "form":form,
        "form1":form1,
        "registered":registered
    }
    return render(request,"registeration.html",context)

def user_login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        # print(username)
        # print(password)
        user=authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse("Please check your creds....")
        
        return HttpResponse("please check your creds....")
        
    return render(request,"login.html",{})


@login_required(login_url='login')
def home_page(request):
    return render(request,"home.html",{})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='login')
def Profile(request):
    profile_data=ModelName.objects.all()
    case_dt=CaseManagement.objects.all()
    return render(request,"userprofile.html",{'profile_data':profile_data,'case_dt':case_dt,})

# @login_required(login_url='login')
def Update(request):
    if request.method=="POST":
        form=UserUpdateForm(request.POST,instance=request.user)
        form1=UserProfileUpdateForm(request.POST,request.FILES,instance=request.user.modelname)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            return redirect('profile')
    else:
        form=UserUpdateForm(instance=request.user) 
        form1=UserProfileUpdateForm(instance=request.user.modelname)   
    return render(request,"update.html",{'form':form,'form1':form1})

# def lawfirm(request):
#     return render(request,"lawhome.html")