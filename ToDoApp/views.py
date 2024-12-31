from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'todoapp/todo.html')

def register(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        #checking the password Length
        if len(password) < 3:
            messages.error(request, 'password at least 3 characters')
            return redirect('register')
        
        #checking if username already exists
        get_all_by_user_name=User.objects.filter(username=username)
        if get_all_by_user_name:
            messages.error(request, 'user name already exists')
            return redirect('register')


        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request,'user created successfully Created')
        return redirect('login')
    return render( request, 'todoapp/registration.html')

def loginPage(request):
    if request.method == 'POST':
        username =request.POST.get('uname')
        password = request.POST.get('pass')

        validateUser=authenticate(username=username,password=password)
        if validateUser is not None:
            login(request,validateUser)
            return redirect('home')
        else:
            messages.error(request, 'invalid username or password')
            return redirect('login')

    return render (request, 'todoapp/login.html')
