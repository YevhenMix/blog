from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from articles.forms import ArticleForm
from articles.models import Article


def all_article_view(request):
    articles = Article.objects.all()
    top_5 = articles[:5]
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {'articles': articles, 'top_articles': top_5}
    return render(request, 'articles/home.html', context)


class ArticleCreateView(SuccessMessageMixin,  LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/create.html'
    success_url = reverse_lazy('main')
    success_message = 'Статья успешно создана!'
    login_url = '/users/login/'


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
    template_name = 'articles/detail.html'
    context_object_name = 'article'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/delete.html'
    success_url = reverse_lazy('main')
    login_url = '/users/login/'


def delete_article(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(id=pk)
        article.delete()
        messages.error(request, 'Статья удалена!')
    return redirect('main')


class ArticleUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'articles/update.html'
    form_class = ArticleForm
    success_url = reverse_lazy('main')
    success_message = 'Статья обновлена!'
    login_url = '/users/login/'
