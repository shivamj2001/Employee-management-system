from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    isActive=True
    if request.method=='POST':
        check=request.POST.get("check")  #we can use POST.get("check") to avoid getting error when no i/p is given and we can get null 
        print(check)
        if check is None: isActive=False
        else: isActive=True
        

    date = datetime.datetime.now()
   
    name="LearnCodeWithDurgesh"
    list_of_programs=[
        'WAP to cheak even or odd',
        'WAP to cheak prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP  to print pascals triangle'
    ]
    student={
        'student_name':"Shivam",
        'student_collage':"JUET",
        'student_city':'LUCKNOW'
    }
    
    # return HttpResponse("<h1>Hello this is index page</h1>" + str(date))
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request,"home.html",data)

def about(request):
    # return HttpResponse("<h1>Hello this is about page</h>")
    return render(request,"about.html",{})

def services(request):
    # return HttpResponse("<h1>Hello this is services page</h>")
    return render(request,"services.html",{})
