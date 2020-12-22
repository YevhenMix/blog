from django.urls import path
from .views import hello, ArticleCreateView, ArticleDetailView

app_name = 'articles'


urlpatterns = [
    path('', hello, name='home'),
    path('create_post/', ArticleCreateView.as_view(), name='create'),
    path('detail_post/<int:pk>', ArticleDetailView.as_view(), name='detail'),
]
