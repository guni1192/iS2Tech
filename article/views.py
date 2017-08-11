from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Article


class IndexView(ListView):
    model = Article
    template_name = 'article/index.html'


class PostArticleView(CreateView):
    model = Article
    fields = ('title', 'detail')
    template_name = 'article/post_article.html'
    success_url = '/article/post'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'


class UpdateArticleView(UpdateView):
    model = Article
    template_name = 'article/post_article.html'
    fields = ('title', 'detail')

    def get_success_url(self):
        return reverse('article:update', args=(self.object.id,))

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'article/article_confirm_delete.html'
    success_url = '/article'
