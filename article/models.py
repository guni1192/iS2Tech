from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=64)
    detail = models.TextField()
    tags = models.CharField(max_length=64, blank=True, null=True)
    types = (('Knowledge', 'Knowledge'),
             ('Product', 'Product'),
             ('Question', 'Question'))

    article_types = models.CharField(
        max_length=10,
        choices=types,
        default='Knowledge',
    )

    is_publish = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=True, blank=True)

    def __str__(self):
        return self.title
