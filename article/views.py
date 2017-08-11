from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Article


class IndexView(ListView):
    model = Article
    template_name = 'article/index.html'


class PostArticleView(CreateView):
    model = Article
    fields = ('title', 'detail')
    template_name = 'article/post_article.html'
    success_url = '/article/post'
