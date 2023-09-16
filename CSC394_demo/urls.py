from django.urls import path
from .views import task_list, add_task, update_task, delete_task

urlpatterns = [
        path('', task_list.as_view(), name='redlobsterTM'),
        path('task/add', add_task.as_view(), name='task_add'),
        path('task/<int:pk>/update/', update_task.as_view(), name='task_update'),
        path('task/<int:pk>/delete/', delete_task.as_view(), name='task_delete')
]
