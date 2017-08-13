from django.conf.urls import url
from . import views

urlpatterns = [
    # Article Type Filter
    url(r'^knowledge$', views.KnowledgeListView.as_view(), name='knowledge'),
    url(r'^products$', views.ProductsListView.as_view(), name='products'),
    url(r'^questions$', views.QuestionsListView.as_view(), name='questions'),

    # Article CRUD
    url(r'^post$', views.PostArticleView.as_view(), name='post_article'),
    url(r'^(?P<pk>\d+)/detail$',
        views.ArticleDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update$',
        views.UpdateArticleView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete$',
        views.DeleteArticleView.as_view(), name='delete'),
]
