from django.conf.urls import url
from .views import PostArticleView, ArticleDetailView, UpdateArticleView, DeleteArticleView

urlpatterns = [
    url(r'^post$', PostArticleView.as_view(), name='post_article'),
    url(r'^(?P<pk>\d+)/detail$', ArticleDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update$', UpdateArticleView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete$', DeleteArticleView.as_view(), name='delete'),
]
