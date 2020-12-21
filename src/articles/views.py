from django.shortcuts import render

from articles.models import Article


def hello(request):
    articles = Article.objects.all()
    top_5 = articles[:6][::-1]
    context = {'articles': articles, 'top_articles': top_5}
    return render(request, 'articles/home.html', context)
