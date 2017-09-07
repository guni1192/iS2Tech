from django.shortcuts import reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CreateAccountView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/user_edit.html'

    def get_success_url(self):
        return reverse('index')


class UpdateAccountView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'accounts/user_edit.html'

    def get_success_url(self):
        return reverse('accounts:edit-user', args=(self.object.id, ))


class UserMyPageView(DetailView):
    model = User
    template_name = 'accounts/user_page_top.html'

