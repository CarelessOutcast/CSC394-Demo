
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
        path('task/<int:pk>/update', views.update_task , name='task_update'),
        path('task/<int:pk>/delete/', views.delete_task, name='task_delete')
]
