from django.shortcuts import render, HttpResponse, redirect
from django import forms
from .models import Category, Article, Comment, CommentReplay , Favourite
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
        fields = ['body']
class CommentReplayForm(forms.ModelForm):
    class Meta:
        model = CommentReplay
        widgets = {
            'body': forms.Textarea(attrs={'cols': 80, 'rows': 20, 'class':'comment-textarea'})
        }
        fields = ['body']

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
    replies_list = {}
    for comment in comments:
        replies = CommentReplay.objects.all().filter(comment=comment.id)
        replies_list[comment.id] = replies
    form_comment = CommentForm()
    form_replay = CommentReplayForm()
    context = { 'article': article, 
                'comments': comments, 
                'replies': replies_list,
                'form_comment': form_comment,
                 'form_replay': form_replay}
    print(context)
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

def add_comment(request, id):
    article = Article.objects.get(id=id) 
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            return redirect('read', id)

def replay_comment(request, id):
    comment = Comment.objects.get(id=id) 
    if request.method == 'POST':
        form = CommentReplayForm(request.POST)
        if form.is_valid():
            replay = form.save(commit=False)
            replay.user = request.user
            replay.comment = comment
            replay.save()
            return redirect('read', id)
