from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

# login page code

def login(request):
   if request.method=='POST':
      uname = request.POST['username']
      password = request.POST['pwd']
      user = auth.authenticate(username=uname,password=password)

      if user is not None:
         auth.login(request,user)
         return redirect('/')
      else:
         # messages.info(request,"Plz enter valid data")
         return redirect('login')
   return render(request,"login.html")

def register(request):
   if request.method=='POST':
      fname=request.POST['fname']
      lname = request.POST['lname']
      mail = request.POST['email']
      uname = request.POST['uname']
      pwd = request.POST['pwd']
      cpwd = request.POST['cpwd']
      if pwd==cpwd:
         if User.objects.filter(username=uname).exists():
            messages.info(request,"Username already exists")
            return redirect("register")
         elif User.objects.filter(email=mail).exists():
            messages.info(request,"Email already exists")
            return redirect("register")
         else:
            user = User.objects.create_user(first_name=fname,last_name=lname,email=mail,username=uname,password=pwd)
            user.save();
            # print("User created successfully...")
            return redirect("login")
      else:
         messages.info(request,"Password mismatching")
         return redirect("register")
      return redirect('/')
   return render(request,"register.html")
def logout(request):
   auth.logout(request)
   return redirect('/')