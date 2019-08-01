from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from blog.models import Article, Comment, CommentForm

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

def blog_show(request, id):
    article = Article.objects.get(pk=id)
    form = CommentForm(request.POST)
    context = {'article': article, 'form': form}
    return render(request, 'show.html', context)
   

def create_comment(request):
    article_id = request.POST['article']
    article = Article.objects.get(id=article_id)
    form = CommentForm()
    context = {"form": form, "message": "Add a comment.", "action": "/comments/create", "article": article}
    # if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.article = article
    form.save()
    return render(request, 'show.html', context)
    # else:
    #     return render(request, 'show.html', context)

    
    # new_comment = Comment()
    # new_comment.name = request.POST['name']
    # new_comment.message = request.POST['message']
    # new_comment.article = article
    # new_comment.save()
    # context = {'article': article}
    # response = render(request, 'show.html', context)
    # return HttpResponse(response) 