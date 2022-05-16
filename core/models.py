from django.db import models
from django.utils.html import strip_tags
import datetime
import math
import re
import readtime

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='Category', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=5000)
    slug = models.SlugField(null=False, unique=True)
    read_time =  models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.title)

    def get_read_time(html_string):
        result = readtime.of_html(html_string)
        return result
        

    def save(self, *args, **kwargs):
        self.read_time = Post.get_read_time(self.body)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name=("Post"), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


