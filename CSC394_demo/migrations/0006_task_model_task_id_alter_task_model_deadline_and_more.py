# Generated by Django 4.2.5 on 2023-09-20 21:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CSC394_demo', '0005_remove_task_model_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_model',
            name='task_id',
            field=models.UUIDField(default=uuid.UUID('62cc88ce-d3e4-4bfb-a1f2-e909251addac'), editable=False),
        ),
        migrations.AlterField(
            model_name='task_model',
            name='deadline',
            field=models.DateTimeField(default='2023-09-20'),
        ),
        migrations.AlterField(
            model_name='task_model',
            name='task',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e81acfe8-747a-4f8b-a773-9b3fcedabdc9'), editable=False, primary_key=True, serialize=False),
        ),
    ]