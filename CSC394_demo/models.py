from django.db import models
import uuid

#creates table in database for user and their information
class user_model(models.Model):
    id = models.UUIDField(
            primary_key = True,
            default     = uuid.uuid4(),
            editable    = False
    )
    first_name  = models.CharField(max_length=100)
    last_name   = models.CharField(max_length=100)
    username    = models.CharField(max_length=50)
    password    = models.CharField(max_length=50)
    email       = models.CharField(max_length=100)

#creates table in database for tasks and their information
class task_model(models.Model):
    # user_id         = models.ForeignKey(user_model, on_delete=models.CASCADE)
    task_id         = models.UUIDField(default=uuid.uuid4(), editable=False)
    # status          = models.CharField(max_length=25, default="To Do")
    name            = models.CharField(max_length=25)
    description     = models.TextField()
    #created_by      = models.CharField(max_length=100)
    created_at      = models.DateTimeField('Created', auto_now_add=True)
    #updated_by      = models.CharField(max_length=100)
    updated_at      = models.DateTimeField('Updated', auto_now=True)
    deadline        = models.DateTimeField()
    #time_remaining  = models.CharField(max_length=25)
    
    def __str__(self):
	    return self.name
    
    

