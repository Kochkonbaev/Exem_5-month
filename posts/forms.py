from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Оглавления', widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label='Текст',widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Post
        fields = ['title', 'body']