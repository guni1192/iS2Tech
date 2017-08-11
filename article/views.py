from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

class IndexView(ListView):
    template_name = 'article/index.html'
    model = Article
