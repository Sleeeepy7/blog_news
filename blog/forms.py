from django import forms

from .models import Comments


class CommentForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'name',
        'placeholder': 'Введите свое имя'
    }))
    email = forms.EmailField(label='почта', widget=forms.EmailInput(attrs={
        'class': 'email',
        'placeholder': 'Введите свою эл. почту'
    }))
    text = forms.CharField(label='комментарий', widget=forms.TextInput(attrs={
        'class': 'comment',
        'placeholder': 'Введите текст'
    }))

    class Meta:
        model = Comments
        fields = ('name', 'email', 'text')
