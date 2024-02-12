from .models import Comment
from django import forms



class  CommentForm(forms.ModelForm):
    class meta:
        model = Comment
        fields = ['name', 'email','body']