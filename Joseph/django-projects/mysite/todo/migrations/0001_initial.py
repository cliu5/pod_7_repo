# Generated by Django 3.2.8 on 2021-10-29 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task', models.CharField(max_length=255)),
            ],
        ),
    ]