
from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="home"),
        path("contact", views.contact, name="contact"),
        path("taskmanager", views.taskmanager, name="taskmanager"),
        path("login", views.login_view, name="login"),
        path("logout", views.logout_view, name="logout"),
        path("add_task/<str:type>", views.add_task, name="add_task"),
        ]
