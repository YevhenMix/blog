from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin

from articles.forms import ArticleForm, CommentForm, ArticleModelForm
from articles.models import Article, Comment

USER = get_user_model()


def all_article_view(request):
    articles = Article.objects.all()
    comments = Comment.objects.all()
    tmp = {}
    for com in comments:            # подсчет всех коментов к отдельному посту
        tmp.setdefault(com.post.id, 0)
        tmp[com.post.id] += 1

    list_d = list(tmp.items())                         # делаем список для дальнейшей сортировки
    list_d.sort(key=lambda i: i[1], reverse=True)       # сортировка по коментам от большего к меньшему

    post_lst = tuple([i[0] for i in list_d[:5]])        # формируем кортеж нужных постов
    comm_count = tuple([i[1] for i in list_d[:5]])      # кортеж с количеством коментов

    top_5 = Article.objects.filter(id__in=post_lst)     # берем из БД нужные посты
    top_5 = [top_5.get(id=pk) for pk in post_lst]       # сортируем их в нужном порядке

    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {'articles': articles, 'top_articles': top_5, 'com_sz': list_d, }
    return render(request, 'articles/home.html', context)


class ArticleCreateView(SuccessMessageMixin,  LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/create.html'
    success_url = reverse_lazy('main')
    success_message = 'Статья успешно создана!'
    login_url = '/users/login/'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = self.form_class()
        if data:
            user = request.user
            name = data['name']
            text = data['text']
            article = Article(name=name, text=text, user=user)
            article.save()
            return redirect('main')

        return render(request, self.template_name, {'form': form})


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
    form_class = ArticleModelForm
    success_url = reverse_lazy('main')
    success_message = 'Статья обновлена!'
    login_url = '/users/login/'


def all_articles_one_user_view(request, pk):
    articles = Article.objects.filter(user=pk)
    user_now = articles[0].user
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {'articles': articles, 'user_now': user_now}
    return render(request, 'articles/all_for_one.html', context)
