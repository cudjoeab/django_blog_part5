"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views 

urlpatterns = [
    path('', views.root), 
    path('admin/', admin.site.urls),
    path('comments/new', views.create_comment, name='create_comment'),
    path('home/', views.home_page, name='home_page'),
    path('article/<int:id>', views.show_article, name='full_article'),
    path('article/<int:id>/edit', views.edit_article, name='edit_article'),
    # path('article/<int:id>/update', views.update_article, name='update_article'),
    path('article/new', views.new_article, name='new_article'), 
    path('article/create', views.create_article, name='create_article'),
    # path('article/<int:id>/delete', views.delete_product, name='delete_product'),
    # #comment paths#
    # path(
    #     "article/<int:product_id>/comments/create",
    #     views.create_comment,
    #     name="create_comment",
    # ),


    # path("article/<int:product_id>/comments/<int:comment_id>/update", views.update_comment, name="update_comment"), 


    # path("article/<int:product_id>/comments/<int:comment_id>/edit", views.edit_comment, name="edit_comment"), 

    # path("article/<int:product_id>/comments/<int:comment_id>/delete", views.delete_comment, name="delete_comment"), 

    
]


