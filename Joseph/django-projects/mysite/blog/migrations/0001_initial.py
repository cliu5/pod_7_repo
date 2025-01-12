# Generated by Django 3.2.8 on 2021-11-04 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('img_link', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('tags', models.ManyToManyField(to='blog.Tag')),
            ],
        ),
    ]
