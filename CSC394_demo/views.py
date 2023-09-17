from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import task_model, user_model
import uuid
from .forms import task_form

import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def taskmanager(request):
    form = task_form() 
    context = {'form':form} 
    return render(request, 'taskmanager.html',context)

def taskmanager1(request):
    form = task_form() 
    context = {'form':form} 
    return render(request, 'taskmanager1.html',context)

def taskmanager2(request):
    form = task_form() 
    context = {'form':form} 
    return render(request, 'taskmanager2.html',context)

def taskmanager3(request):
    form = task_form() 
    context = {'form':form} 
    return render(request, 'taskmanager3.html',context)

def taskmanager4(request):
    form = task_form() 
    context = {'form':form} 
    return render(request, 'taskmanager4.html',context)

def taskmanager5(request):
    form = task_form() 
    context = {'form':form} 
    return render(request, 'taskmanager5.html',context)

def taskmanager6(request):
    form = task_form() 
    context = {'form':form} 
    return render(request, 'taskmanager6.html',context)

def taskmanager7(request):
    form = task_form() 
    context = {'form':form} 
    return render(request, 'taskmanager7.html',context)

def taskmanager8(request):
    form = task_form() 
    context = {'form':form} 
    return render(request, 'taskmanager8.html',context)

def taskmanager9(request):
    form = task_form() 
    context = {'form':form} 
    return render(request, 'taskmanager9.html',context)

def taskmanager10(request):
    form = task_form() 
    context = {'form':form} 
    return render(request, 'taskmanager10.html',context)

def taskmanager11(request):
    form = task_form() 
    context = {'form':form} 
    return render(request, 'taskmanager11.html',context)

def taskmanager12(request):
    form = task_form() 
    context = {'form':form} 
    return render(request, 'taskmanager12.html',context)



#insert
def add_task(request):
    add_task_object = request.POST
    user_first_name = add_task_object['first_name']
    user_last_name  = add_task_object['last_name']
    deadline        = add_task_object['deadline']
    task_model.objects.create(
        user_id         = add_task_object['user_id'],
        task_id         = uuid.uuid4(),
        name            = add_task_object['name'],
        description     = add_task_object['description'],
        created_by      = user_first_name + '' + user_last_name,
        updated_by      = user_first_name + '' + user_last_name,
        deadline        = deadline,
        time_remaining  = str(round(((deadline - datetime.now()).total_seconds())/3600), 2) + ' Hours'
    )
    return redirect('taskmanager')
    
#update
def update_task(request, task_id):
    task = get_object_or_404(task_model, pk=task_id)
    update_task_object = request.POST
    task_model.objects.filter(task_id).update(
        status          = update_task_object['status'],
        name            = update_task_object['name'],
        description     = update_task_object['description'],
        updated_by      = update_task_object['updated_by'],
        deadline        = update_task_object['deadline'],
        time_remaining  = update_task_object['time_remaining']
    )
    return redirect('taskmanager')
    
#delete
def delete_task(request, task_id):
    task = get_object_or_404(task_model, pk=task_id)
    task.delete()
    return redirect('taskmanager')



def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("main_app"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))



def main_app(request):
    # Check if user is logged in
    if request.user.is_authenticated:
        column_keys = list(reversed(range(0, 7)))
        user_habits = request.user.habits.all()

        # Create a list of the user's habits
        user_habits_list = request.user.habits.all().\
            values_list("name", flat=True)

        # Get error message parameter from add_habit()
        message = request.GET.get("message")
        # If message is None (no error), clear the variable
        if message is None:
            message = ""

        return render(request, "main_app.html", {
            "column_keys": column_keys,
            "user_task": user_habits,
            "message": message
        })
    else:
        return render(request, "index.html")



