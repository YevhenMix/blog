from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    name = forms.CharField(label='Заголовок',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите название статьи'}))
    text = forms.CharField(label='Наполнение',
                           widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'placeholder': 'Напишите статью'}))

    class Meta:
        model = Article
        fields = ('name', 'text',)
