from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect 
from django.urls import reverse 
from blog.models import Article, Comment, CommentForm, ArticleForm

def root(request):
    return HttpResponseRedirect('/home')

def home_page(request):
    # context = {}

    context = { 
    'articles': Article.objects.all().order_by('-published_date'),
    'current_time': datetime.now() 
    }
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def show_article(request, id):
    article = Article.objects.get(pk=id)
    form = CommentForm()
    context = {'article': article, 'form': form}
    return render(request, 'show.html', context)

def new_article(request):
    form = ArticleForm()
    context = {"form": form}
    return render(request, 'create_article.html', context)
   
     
def create_article(request): #saving article to database 
        form = ArticleForm(request.POST)
        context = {"form": form}
        if form.is_valid(): 
            form.save()
            return render(request, 'index.html', context)
        else:
            context = {"form": form}
            return render(request, 'index.html', context)

def edit_article(request, id):  # Renders a form to edit an existing article.
    article =Article.objects.get(pk=id)
    form =ArticleForm(instance=article)
    context = {"product":article, "form": form}
    return render(request, "edit_product_form.html", context)

def create_comment(request):
    article_id = request.POST['article']
    article = Article.objects.get(id=article_id)
    form = CommentForm(request.POST)
    new_comment = form.save(commit=False)
    new_comment.article = article
    context = {"form": form, "message": "Add a comment.", "action": "/comments/create", "article": article}
    form.save()
    form = CommentForm()
    return render(request, 'show.html', context)

