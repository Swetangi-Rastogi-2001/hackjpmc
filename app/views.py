from django.shortcuts import render
from . import forms 
from . import models


# Create your views here.

def Home(request):
    return render(request, 'home.html')


def profiling_attempt(request):
    
    if request.method =='POST':
        print("If works")
        form = forms.CheckConditions(request.POST)

        result= models.UserData.objects.all()
        some_var = request.POST.getlist('checks')

        print(some_var)
        return render(request, "success.html")
        
        # if form.is_valid():
        #     result= models.UserData.objects.all()
        #     some_var = request.POST.getlist('checks')

        #     print(some_var)
        #     return render(request, "success.html")

            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email_id = form.cleaned_data['email_id']
            # contact_number = form.cleaned_data['contact_number']


            # models.UserData.objects.create(first_name= first_name, last_name= last_name, email_id= email_id, contact_number= contact_number)
            # return render(request, "success.html")
            #print(first_name, last_name, email_id, contact_number)

        # else:
        #     print("Wrong Inputs")
        #     #grab from front and save in database

    else:
        print("Else works")
        #display form on frontend
        form = forms.CheckConditions()
        return render(request, 'Profiling.html', {"form":form})


def female(request):
    data = models.UserData.objects.filter(sex="Female")
    return render(request, "display.html", {"data":data})

def male(request):
    data = models.UserData.objects.filter(sex="Male")
    return render(request, "display.html", {"data":data})


def female_cruthces(request):
    data = models.UserData.objects.filter(sex="Female", cruthces="Yes")
    return render(request, "display.html", {"data":data})

def male_cruthces(request):
    data = models.UserData.objects.filter(sex="Male", cruthces= "Yes")
    return render(request, "display.html", {"data":data})




        
