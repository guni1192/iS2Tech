from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'title',
            'detail',
            'article_types',
            'is_publish',
            )
        widgets = {
            'detail': forms.Textarea(attrs={
                'id': 'md_editor',
                'v-model': 'md_editor',
                'debounce': '100'
            }),
        }

