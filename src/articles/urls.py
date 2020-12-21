from django.urls import path
from .views import hello

app_name = 'articles'


urlpatterns = [
    path('', hello, name='home')
]
