from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()


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


class Comment(models.Model):
    text = models.CharField(max_length=300)
    user = models.ManyToManyField(USER, verbose_name='Коментарии')
    post = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-pub_date']
