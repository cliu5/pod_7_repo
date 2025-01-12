from django.db import models

# Create your models here.


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    img_link = models.URLField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    post = models.ForeignKey(
        Post, blank=True, null=True, on_delete=models.CASCADE)
