from django.shortcuts import render

# Create your views here.
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

    print(article)
    return render(request, 'blog/article.html', {
        'article': article
    })