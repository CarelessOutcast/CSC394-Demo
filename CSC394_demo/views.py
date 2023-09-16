from django.shortcuts import render
from .models import task_model

# Create your views here.

def index(request):
    return render(request,'redlobsterHome.html')

#insert
def add_task(request):
    task_title = request.POST['task_title']
    task_model.objects.create(task_title=task_title)
    return 
    
#update
def update_task(request):
    pass

#delete
def delete_task(request):
    pass