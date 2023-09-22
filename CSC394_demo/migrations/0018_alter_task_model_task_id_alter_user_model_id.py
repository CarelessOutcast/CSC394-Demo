# Generated by Django 4.2.5 on 2023-09-22 18:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CSC394_demo', '0017_alter_task_model_task_id_alter_user_model_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_model',
            name='task_id',
            field=models.BigIntegerField(default=19727609955182277966112998895, editable=False),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('57873e56-2c6e-4ec6-b5fd-095b1649121f'), editable=False, primary_key=True, serialize=False),
        ),
    ]