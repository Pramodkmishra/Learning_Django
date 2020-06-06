from django.shortcuts import render,HttpResponse
from .models import UserDetail 
def registerForm(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        mname=request.POST['middlename']
        lname=request.POST['lastname']
        cour=request.POST['sub']
        gender=request.POST['gender']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        password1=request.POST['psw']
        password2=request.POST['psw_repeat']

        if password1==password2:
            obj=UserDetail(first_name=fname,middle_name=mname,last_name=lname,course=cour,gender=gender,phone=phone,email=email,address=address,password=password1)
            obj.save()
            print("object save")
            
            
        else:
            print("password missmatch")


        print(fname,cour,address)
        return HttpResponse("<h1>post</h1>")
    else:
        return render(request,'registrationForm.html')

def hh(request):
    return HttpResponse("<h1>hhhh</h1>")

# Create your views here.
