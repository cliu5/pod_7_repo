# Generated by Django 3.2.8 on 2021-11-05 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todolist_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='completed',
            field=models.BooleanField(),
        ),
    ]
