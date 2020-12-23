from django.db import models
from django.utils import timezone


class Article(models.Model):
    name = models.CharField(max_length=250, unique=True)
    text = models.TextField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-create_date']
