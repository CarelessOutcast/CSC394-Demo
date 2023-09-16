from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import task_model, user_model

import random
import datetime

# Create your views here.

def index(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def taskmanager(request):
    return render(request,'taskmanager.html')

#insert
def add_task(request):
    task_title = request.POST['task_title']
    task_model.objects.create(task_title=task_title)
    return 
    
#update
def update_task(request):
    pass

#delete
def delete_task(request, person, habit_id):
    pass



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
            "user_habits": user_habits,
            "message": message
        })
    else:
        return render(request, "index.html")



