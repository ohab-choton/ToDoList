from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ToDo
from django.contrib.auth.decorators import login_required


# Create your views here.
#send data to database 
@login_required
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':  
        task=request.POST.get('task')
        if task.strip():
            new_todo=ToDo(user=request.user,todo_name=task)
            new_todo.save()
            # iexact means case comparison
    all_todos = ToDo.objects.filter(user=request.user).exclude(todo_name__iexact='').exclude(todo_name__exact=' ')
    return render(request, 'todoapp/todo.html',{'all_todos':all_todos})

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

# views.py
def logoutPage(request):    
    logout(request)
    return redirect('login')


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

def deleteTask(request,name):
    if not request.user.is_authenticated:
        return redirect('login')
    get_todo=ToDo.objects.filter(user=request.user,todo_name=name)
    get_todo.delete()
    return redirect('home')
    

def updateTask(request,name):
    if not request.user.is_authenticated:
        return redirect('login')
    get_todo= ToDo.objects.get(user=request.user,todo_name=name)
    get_todo.status = True
    get_todo.save()
    return redirect('home')
    