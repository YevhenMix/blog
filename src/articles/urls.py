from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (all_article_view, delete_article, save_comment_view,
                    ArticleCreateView, ArticleDetailView, ArticleDeleteView, ArticleUpdateView)

app_name = 'articles'


urlpatterns = [
    path('', all_article_view, name='home'),
    path('create_post/', ArticleCreateView.as_view(), name='create'),
    path('detail_post/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('delete_post/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('delete_cor/<int:pk>', delete_article, name='delete_cor'),
    path('update_post/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('save/', save_comment_view, name='save'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
