from .models import Post, Comment #Comment追加

# Create your views here.
from django.shortcuts import render, redirect
from . import forms #この行追加
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'posts': posts
    })

# 記事専用の子ページ
def article(request, pk):
    article = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=article)

    if request.method == "POST": #入力フォームはPOSTなので
        form = forms.CommentForm(request.POST)
        if form.is_valid(): #もし、formの内容が正しい時は
            comment = form.save(commit=False) #formの内容はまだセーブしません！
            comment.post = article
            comment.author = request.user
            comment.save() #ユーザーを追加したのちにセーブ
    else:
        form = forms.CommentForm()

    print(article)
    return render(request, 'blog/article.html', {
        'article': article,
        'form': form,
        'comments': comments
    }) #form と comment　を追加

def delete_comment(request, pk, comment_pk):    # pk:記事自体の番号、comment_pk:コメントの番号
    comment = Comment.objects.get(id=comment_pk)
    post_id = pk
    # 削除リクエストのユーザid == コメントの筆者(loginid)かポスト(記事)の筆者
    if request.user.id == comment.author.id or \
       request.user.id == comment.post.author.id:
        comment.delete()
    return redirect('blog:article', pk=post_id)
    
def create_article(request):
    form = forms.PostForm()
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('blog:article', pk=post.id)

    return render(request, 'blog/create_article.html', {
        'form': form
    })