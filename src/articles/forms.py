from django import forms
from .models import Article, Comment


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


class CommentForm(forms.Form):
    text = forms.CharField(label='Коментарий',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Оставьте комментарий'}))


class CommentModelForm(forms.ModelForm):
    text = forms.CharField(widget=forms.HiddenInput)
    user = forms.CharField(widget=forms.HiddenInput)
    post = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Comment
        fields = ('text', 'user', 'post')
