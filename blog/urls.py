from django.urls import path
from . import views

app_name = 'blog' #django2.0から必要になったnamespace定義
urlpatterns = [
    path('', views.post_list, name='post_list'),
	path('article/<int:pk>/', views.article, name='article'),	# 追加
    path('article/<int:pk>/comment-delete/<int:comment_pk>/', views.delete_comment, name='delete_comment'),
]