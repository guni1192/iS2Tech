from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=64)
    detail = models.TextField()
    tags = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.title

