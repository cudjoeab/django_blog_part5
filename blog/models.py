from datetime import datetime 
from django.contrib.auth.models import User
from django.db import models 
from django.forms import ModelForm

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    draft = models.BooleanField(default=True)
    published_date= models.DateTimeField(default=datetime.now, blank=True)
    author= models.CharField(max_length=255)

    def __str__(self):
        return (f'{self.title}, By: {self.author}') 

class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']
