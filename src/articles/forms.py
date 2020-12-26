from django import forms
from .models import Article, Comment


class ArticleForm(forms.Form):
    name = forms.CharField(label='Заголовок',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите название статьи'}))
    text = forms.CharField(label='Наполнение',
                           widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'placeholder': 'Напишите статью'}))
    user = forms.CharField(widget=forms.HiddenInput)


class ArticleModelForm(forms.ModelForm):
    name = forms.CharField(label='Заголовок',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите название статьи'}))
    text = forms.CharField(label='Наполнение',
                           widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'placeholder': 'Напишите статью'}))

    class Meta:
        model = Article
        fields = ('name', 'text',)


class CommentForm(forms.Form):
    text = forms.CharField(label='Коментарий',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Оставьте комментарий'}))
