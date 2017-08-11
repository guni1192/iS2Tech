from django.conf.urls import url
from .views import IndexView, PostArticleView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^post$', PostArticleView.as_view(),
        name='post_article'),
]
