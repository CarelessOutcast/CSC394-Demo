from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView 
from .models import task_model


# Create your views here.

def index(request):
    return render(request,'redlobsterHome.html')

#list
def task_list(list_view):
    model           = task_model
    template_name   = 'redlobsterHome.html'
    
#insert
def add_task(CreateView):
    model           = task_model
    template_name   = 'task_add.html'
    fields          = '__all__'
    success_url     = redirect('redlobsterTM')
    
#update
def update_task(UpdateView):
    model           = task_model
    template_name   = 'task_update.html'
    fields          = '__all__'
    success_url     = redirect('redlobsterTM')
    
#delete
def delete_task(DeleteView):
    model           = task_model
    template_name   = 'task_delete.html'
    success_url     = redirect('redlobsterTM')