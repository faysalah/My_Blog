from django.shortcuts import render, HttpResponse, redirect
from django import forms
from .models import Category, Article, Comment
from django.contrib.auth.models import User
# Create your views here.
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
        fields = '__all__'

def index(request):
    articles = Article.objects.all()
    return render(request, 'article/index.html',{ 'articles': articles })

def create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = AtricleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/article')
    else:
         form = AtricleForm()
    return render(request,'article/create.html',{'form':form ,'category': categories })

def read(request, id ):
    article = Article.objects.get(id=id)
    comments = Comment.objects.all().filter(article=id)
    form = CommentForm()
    context = {'article': article, 'comments': comments, 'form': form }
    return render(request, 'article/read.html', context)

def edit(request, id ):
    article = Article.objects.get(id=id)
    if request.method == "POST":
        form = AtricleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('/article')
    else:
        form = AtricleForm(instance=article)
        context = {'form': form }
        return render(request, 'article/edit.html', context)
