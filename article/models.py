from django.db import models


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

    def __str__(self):
        return self.title
