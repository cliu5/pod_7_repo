# Generated by Django 3.2.9 on 2021-11-04 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('note_id', models.AutoField(primary_key=True, serialize=False)),
                ('note_text', models.CharField(max_length=255)),
            ],
        ),
    ]
