from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    if request.method=='POST':
        print("hello login")
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are now logged in')
            return redirect('home')
        else:
            messages.error(request,'invalid credantials')
            return redirect('login')
        #return redirect('login')
    else:
        return render(request,'accounts/login.html')
def register(request):
    if request.method=='POST':
        #print('hello register')
        #get values from request
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            #check Username
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already being used')
                    return redirect('register')
                else:
                    #looks like good
                    user=User.objects.create_user(first_name=first_name,last_name=last_name,
                    username=username,password=password,email=email)
                    #login after registration
                    #auth.login(request,user)
                    #messages.success(request,'you are logged in')
                    #return redirect('home')
                    user.save()
                    messages.success(request,'you are successfully registered ')
                    return rediect('login')
        else:
            messages.error(request,'password did not match')
            return render(request,'accounts/register.html')
    else:
        return render(request,'accounts/register.html')
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'logout successfully')
        return redirect('home')
def dashboard(request):
    return render(request,'accounts/dashboard.html')
