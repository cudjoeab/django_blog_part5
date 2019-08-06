from datetime import datetime 
from django.utils.timezone import timezone
from django.contrib.auth.models import User
from django.db import models 
from django.forms import ModelForm
from django.core.validators import MinLengthValidator

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    body = models.TextField(validators = [MinLengthValidator(1)], null=True)
    draft = models.BooleanField(default=True)
    published_date= models.DateTimeField(default=datetime.now, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return (f'{self.title}, By: {self.author}') 

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author','body','draft','published_date']

class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']
