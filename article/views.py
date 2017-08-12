from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Article
from .forms import ArticleModelForm


class IndexView(ListView):
    model = Article
    template_name = 'article/index.html'


class PostArticleView(CreateView):
    form_class = ArticleModelForm
    template_name = 'article/post_article.html'
    success_url = '/article/post'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'


class UpdateArticleView(UpdateView):
    form_class = ArticleModelForm
    template_name = 'article/post_article.html'

    def get_success_url(self):
        return reverse('article:update', args=(self.object.id,))


class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'article/article_confirm_delete.html'
    success_url = '/article'
