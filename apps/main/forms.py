from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)

class CommentForm(forms.ModelForm):
    content = forms.FileField()
    class Meta:
        model = Comment
        fields = ('content',)
