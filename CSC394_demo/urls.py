
from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="home"),
        path("contact", views.contact, name="contact"),
        path("login", views.login_view, name="login"),
        path("logout", views.logout_view, name="logout"),
        path("taskmanager", views.taskmanager, name="taskmanager"),
        path("taskmanager1", views.taskmanager1, name="taskmanager1"),
        path("taskmanager2", views.taskmanager2, name="taskmanager2"),
        path("taskmanager3", views.taskmanager3, name="taskmanager3"),
        path('add', views.add_task, name='task_add'),
        #"str:id" is the variable that is passed along from the object on the screen to the database to find the correct object
        path('update/<str:id>', views.update_task , name='update_task'), 
        path('delete/<str:id>', views.delete_task, name='delete_task')
]
