from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect 
from django.urls import reverse 
from blog.models import Article, Comment, CommentForm, ArticleForm

def root(request):
    return HttpResponseRedirect('/home')

def home_page(request):
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
    return render(request, 'article.html', context)

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
            return render(request, 'create_article.html', context)

def edit_article(request, id):  # Renders a form to edit an existing article.
    article = Article.objects.get(pk=id)
    form = ArticleForm(instance=article)
    context = {"product":article, "form": form}
    return render(request, "edit_article_form.html", context)

def update_article(request, id):  # User updating an existing product.
    article = Article.objects.get(pk=id)
    form = ArticleForm(request.POST, instance=article)
    context = {"article": article, "form": form}
    if form.is_valid():
        form.save()
        return render(request, 'index.html', context)
    else:  # Else sends user back to existing product form.
        context = {"article": article, "form": form}
        return render(request, "edit_article_form.html", context)

def delete_article(request, id):  # User deleting an existing product.
    article = Article.objects.get(pk=id)
    article.delete()
    return redirect(reverse("home_page"))

def create_comment(request):
    article_id = request.POST['article']
    article = Article.objects.get(id=article_id)
    form = CommentForm(request.POST)
    new_comment = form.save(commit=False)
    new_comment.article = article
    context = {"form": form, "message": "Add a comment.", "action": "/comments/create", "article": article}
    form.save()
    form = CommentForm()
    return render(request, 'article.html', context)

def edit_comment(request, article_id, comment_id):
    article = Article.objects.get(pk=product_id)
    comment = Review.objects.get(pk=product_id)
    comment.article_id = comment_id
    form = CommentForm(instance=comment)
    context = {"comment": comment, "form": form, "article": article}
    return render(request, "edit_comment_form.html", context)

def update_comment(request, article_id, comment_id): 
    comment = Comment.objects.get(pk=review_id)
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
        form.save()
        return render(request, 'article.html', context)
    else: 
        context = {"comment": comment, "form": form, "product": product}
        return render(request, "edit_comment_form.html", context)

def delete_comment(request, article_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect(reverse("article.html", kwargs={"id":article_id}))