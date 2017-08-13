from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Article
from .forms import ArticleModelForm


@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    template_name = 'article/index.html'
    queryset = Article.objects.filter(is_publish=True).order_by('created_date', 'title')


@method_decorator(login_required, name='dispatch')
class KnowledgeListView(ListView):
    template_name = 'article/index.html'
    queryset = Article.objects.filter(is_publish=True,
                                      article_types='Knowledge')


@method_decorator(login_required, name='dispatch')
class ProductsListView(ListView):
    template_name = 'article/index.html'
    queryset = Article.objects.filter(is_publish=True,
                                      article_types='Product')


@method_decorator(login_required, name='dispatch')
class QuestionsListView(ListView):
    template_name = 'article/index.html'
    queryset = Article.objects.filter(is_publish=True,
                                      article_types='Question')


@method_decorator(login_required, name='dispatch')
class PostArticleView(CreateView):
    form_class = ArticleModelForm
    template_name = 'article/post_article.html'
    success_url = '/article/post'


@method_decorator(login_required, name='dispatch')
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'


@method_decorator(login_required, name='dispatch')
class UpdateArticleView(UpdateView):
    form_class = ArticleModelForm
    model = Article
    template_name = 'article/post_article.html'

    def get_success_url(self):
        return reverse('article:update', args=(self.object.id,))


@method_decorator(login_required, name='dispatch')
class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'article/article_confirm_delete.html'
    success_url = '/'
