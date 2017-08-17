from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_change, password_change_done
from django.urls import reverse_lazy
from .views import CreateAccountView, UpdateAccountView, UserMyPageView

urlpatterns = [
    url(r'^login/$', login,
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^create/user/$',
        CreateAccountView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        UpdateAccountView.as_view(), name='update'),
    url(r'^password/change/$',
        password_change,
        {
            'post_change_redirect': reverse_lazy('accounts:pwd_change_done'),
            'template_name': 'accounts/password_change_form.html',
        },
        name='pwd_change'
        ),

    url(r'^password/changeed/$',
        password_change_done,
        {
            'template_name': 'accounts/password_change_done.html',
        },
        name='pwd_change_done'
        ),
    url(r'^(?P<pk>[0-9]+)/mypage/$',
        UserMyPageView.as_view(), name='mypage'),

]
