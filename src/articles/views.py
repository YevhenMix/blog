from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin

from articles.forms import ArticleForm, CommentForm
from articles.models import Article, Comment

USER = get_user_model()


def all_article_view(request):
    articles = Article.objects.all()
    auths = USER.objects.all()
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


class ArticleDetailView(FormMixin, DetailView):
    queryset = Article.objects.all()
    template_name = 'articles/detail.html'
    context_object_name = 'article'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = {'article': Article.objects.get(id=pk),
                   'comments': Comment.objects.filter(post=pk),
                   'form': CommentForm, }
        return context


def save_comment_view(request):
    if request.method == 'POST':
        data = request.POST
        if data:
            text = data['text']
            user = USER.objects.filter(id=int(data['user']))
            post = Article.objects.get(id=int(data['post']))
            comment = Comment(text=text, post=post)
            comment.save()
            comment.user.set(user)
    return redirect(f"/articles/detail_post/{request.POST['post']}")


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


