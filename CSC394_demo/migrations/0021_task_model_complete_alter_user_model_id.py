# Generated by Django 4.2.5 on 2023-09-22 18:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CSC394_demo', '0020_alter_user_model_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_model',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9ac4706c-8507-427f-b203-9089fbbedcc0'), editable=False, primary_key=True, serialize=False),
        ),
    ]
