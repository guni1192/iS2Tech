from django.db import models
from django.utils import timezone


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

    published_date = models.DateField(blank=True, null=True)
    is_publish = models.BooleanField()

    def publich(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
