from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        username=request.POST['user']
        Email=request.POST['email']
        Password=request.POST['pswf']
        Re_password=request.POST['psws']

        if Password==Re_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request,"Email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=Email,password=Password)
                user.save();
                print("user created")
        else:
            messages.info(request,"Incorrect Password")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid details")
            return redirect('login')
    else:        
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')