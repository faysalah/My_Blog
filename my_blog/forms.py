from django import forms
from .models import Category, Article, Comment, CommentReplay , Favourite


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'info': forms.Textarea(attrs={'cols': 80, 'rows': 20, 'class':'materialize-textarea'})
        }
class AtricleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'body': forms.Textarea(attrs={'cols': 80, 'rows': 20, 'class':'materialize-textarea'})
        }
        fields = '__all__'
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            'body': forms.Textarea(attrs={'cols': 80, 'rows': 20, 'class':'comment-textarea'})
        }
        fields = ['body']
class CommentReplayForm(forms.ModelForm):
    class Meta:
        model = CommentReplay
        widgets = {
            'body': forms.Textarea(attrs={'cols': 80, 'rows': 20, 'class':'comment-textarea'})
        }
        fields = ['body']