from lawfirmapp import views
from django.urls import path


urlpatterns = [
    path('',views.home,name='law'),
    path('lawprofile',views.lawprofile,name='lawprofile'),
    path('about',views.about,name='about'),
    path('allCases',views.allCases,name='allCases'),
    path('enquiry',views.enquiry,name='enquiry'),
    path('appointment',views.appointment,name='appointment'),
    path('contact',views.contact,name='contact')
]
