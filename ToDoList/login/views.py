from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Todo

# Create your views here.
def home(request):
       if request.method == 'POST':
              task_name = request.POST.get('task')
              todo = Todo(user=request.user, name=task_name)
              todo.save()
       
       toDos = Todo.objects.filter(user=request.user)
       context = {
              'toDos' : toDos
       }
       
       print(context)
              
       return render(request, 'login/todo.html', context)

def register(request):
       if request.method == 'POST':
              username = request.POST.get('username')
              email = request.POST.get('email')
              password = request.POST.get('password')
              
              if len(password) < 3:
                     messages.error(request, 'password must be more than 3 characters')
                     return redirect('register')
              
              users_name = User.objects.filter(username=username)
              if users_name:
                     messages.error(request, 'user name already exists')
                     return redirect('register')
              
              user = User.objects.create_user(username=username, email=email, password=password)
              user.save()
              messages.success(request, 'user successfully created')
              return redirect('loginPage')
              
       return render(request, 'login/register.html', {})

def loginPage(request):
       if request.method == 'POST':
              username = request.POST.get('uname')
              password = request.POST.get('pass')
              
              user_validate = authenticate(username=username, password=password)
              
              if user_validate is not None:
                     login(request, user_validate)
                     return redirect('homePage')
              else:
                     messages.error(request, 'user doesn\'t exists')
                     return redirect('loginPage')
              
       return render(request, 'login/login.html', {})

def delete(request, name):
       the_todo = Todo.objects.get(user=request.user, name=name)
       the_todo.delete()
       return redirect('homePage')

def complete(request, name):
       the_todo = Todo.objects.get(user=request.user, name=name)
       the_todo.status = True
       the_todo.save()
       return redirect('homePage')
