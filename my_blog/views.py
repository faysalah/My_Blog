from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CategoryForm, AtricleForm, CommentForm, CommentReplayForm
from .models import Category, Article, Comment, CommentReplay, Favourite

def index(request):
    articles = Article.objects.all().filter(is_publish=1)
    return render(request, 'article/index.html',{ 'articles': articles })

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def read(request, id ):
    article = Article.objects.get(id=id)
    comments = Comment.objects.all().filter(article=id)
    is_favoruite = False
    replies_list = {}
    if Favourite.objects.filter(article=id,user=request.user.id).exists():
        is_favoruite = True
    for comment in comments:
        replies = CommentReplay.objects.all().filter(comment=comment.id)
        replies_list[comment.id] = replies
    form_comment = CommentForm()
    form_replay = CommentReplayForm()
    context = { 'article': article, 
                'comments': comments, 
                'replies': replies_list,
                'form_comment': form_comment,
                'form_replay': form_replay,
                'is_favourite': is_favoruite }
    print(context)
    return render(request, 'article/read.html', context)

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def do_favourite(request, id):
    if request.method == 'POST':
        if not Favourite.objects.filter(article=id,user=request.user.id).exists():
            favourite = Favourite(user=User.objects.get(id=request.user.id),article=Article.objects.get(id=id))
            favourite.save()
        else:
            Favourite.objects.filter(user=request.user.id,article=id).delete()
    return redirect('read', id)

@login_required(login_url='/accounts/login/')
def published(request):
    articles = Article.objects.all().filter(is_publish=1,author=request.user.id)
    return render(request, 'article/index.html',{ 'articles': articles })
    
@login_required(login_url='/accounts/login/')
def drafts(request):
    articles = Article.objects.all().filter(is_publish=0,author=request.user.id)
    return render(request, 'article/index.html',{ 'articles': articles })
