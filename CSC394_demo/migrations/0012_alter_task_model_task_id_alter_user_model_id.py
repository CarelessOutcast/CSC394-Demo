# Generated by Django 4.2.5 on 2023-09-22 17:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CSC394_demo', '0011_alter_task_model_task_id_alter_user_model_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_model',
            name='task_id',
            field=models.UUIDField(default=68585227906006275715529069049268353201, editable=False),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a7c256d5-e676-4c32-98fe-aadf679b6fb6'), editable=False, primary_key=True, serialize=False),
        ),
    ]