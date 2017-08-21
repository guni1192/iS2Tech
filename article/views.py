from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Article
from .forms import ArticleModelForm


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'article/index.html'
    queryset = Article.objects \
        .filter(is_publish=True) \
        .order_by('-created_date', 'title')


class KnowledgeListView(LoginRequiredMixin, ListView):
    template_name = 'article/index.html'
    queryset = Article.objects \
        .filter(is_publish=True, article_types='Knowledge') \
        .order_by('-created_date', 'title')


class ProductsListView(LoginRequiredMixin, ListView):
    template_name = 'article/index.html'
    queryset = Article.objects \
        .filter(is_publish=True, article_types='Product') \
        .order_by('-created_date', 'title')


class QuestionsListView(LoginRequiredMixin, ListView):
    template_name = 'article/index.html'
    queryset = Article.objects \
        .filter(is_publish=True, article_types='Question') \
        .order_by('-created_date', 'title')


class PostArticleView(LoginRequiredMixin, CreateView):
    form_class = ArticleModelForm
    template_name = 'article/post_article.html'
    success_url = '/article/post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, '投稿しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, '投稿に失敗しました。')
        return super().form_invalid(form)



class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article/detail.html'


class UpdateArticleView(LoginRequiredMixin, UpdateView):
    form_class = ArticleModelForm
    model = Article
    template_name = 'article/post_article.html'

    def get_success_url(self):
        return reverse('article:update', args=(self.object.id,))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteArticleView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article/article_confirm_delete.html'
    success_url = '/'
