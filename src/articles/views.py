from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from articles.forms import ArticleForm
from articles.models import Article


def hello(request):
    articles = Article.objects.all()
    max_s = len(articles) - 6
    top_5 = articles[max_s:][::-1]
    context = {'articles': articles, 'top_articles': top_5}
    return render(request, 'articles/home.html', context)


class ArticleCreateView(SuccessMessageMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/create.html'
    success_url = reverse_lazy('main')
    success_message = 'Пост успешно создан!'


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
    template_name = 'articles/detail.html'
    context_object_name = 'article'
